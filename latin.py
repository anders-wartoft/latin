#!/usr/bin/env python3
"""
LATIN Interpreter - Latin Ain't This Insufferable Normally
A minimal interpreter for the LATIN programming language.
"""

import re
import sys
from typing import Dict, List, Optional, Tuple


class RomanNumeralParser:
    """Parse Roman numerals to integers."""
    
    ROMAN_VALUES = {
        'M': 1000, 'D': 500, 'C': 100, 'L': 50,
        'X': 10, 'V': 5, 'I': 1
    }
    
    @classmethod
    def parse(cls, roman: str) -> Optional[int]:
        """Convert a Roman numeral string to an integer."""
        if not roman:
            return None
        
        total = 0
        prev_value = 0
        
        for char in reversed(roman):
            if char not in cls.ROMAN_VALUES:
                return None
            
            value = cls.ROMAN_VALUES[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        
        return total if total > 0 else None


class LatinDeclension:
    """Handle Latin noun declensions."""
    
    # Dictionary mapping nominative forms to their declined forms
    # Format: nominative -> {accusative, dative, ablative}
    # Note: In 2nd declension, dative and ablative singular are the same
    DECLENSIONS = {
        'NUMERUS': {'acc': 'NUMERUM', 'dat': 'NUMERO', 'abl': 'NUMERO'},
        'PRIMUS': {'acc': 'PRIMUM', 'dat': 'PRIMO', 'abl': 'PRIMO'},
        'SECUNDUS': {'acc': 'SECUNDUM', 'dat': 'SECUNDO', 'abl': 'SECUNDO'},
        'TERTIUS': {'acc': 'TERTIUM', 'dat': 'TERTIO', 'abl': 'TERTIO'},
        'AMICUS': {'acc': 'AMICUM', 'dat': 'AMICO', 'abl': 'AMICO'},
        'PUELLA': {'acc': 'PUELLAM', 'dat': 'PUELLAE', 'abl': 'PUELLA'},
        'BELLUM': {'acc': 'BELLUM', 'dat': 'BELLO', 'abl': 'BELLO'},
        'RES': {'acc': 'REM', 'dat': 'REI', 'abl': 'RE'},
        'SUMMA': {'acc': 'SUMMAM', 'dat': 'SUMMAE', 'abl': 'SUMMA'},
    }
    
    @classmethod
    def get_nominative(cls, declined_form: str) -> Optional[str]:
        """Get the nominative form of a declined noun."""
        # Check if it's already nominative
        if declined_form in cls.DECLENSIONS:
            return declined_form
        
        # Search through declensions
        for nom, forms in cls.DECLENSIONS.items():
            if declined_form in forms.values():
                return nom
        
        return None
    
    @classmethod
    def get_accusative(cls, nominative: str) -> Optional[str]:
        """Get the accusative form of a noun."""
        return cls.DECLENSIONS.get(nominative, {}).get('acc')
    
    @classmethod
    def get_dative(cls, nominative: str) -> Optional[str]:
        """Get the dative form of a noun."""
        return cls.DECLENSIONS.get(nominative, {}).get('dat')
    
    @classmethod
    def get_ablative(cls, nominative: str) -> Optional[str]:
        """Get the ablative form of a noun."""
        return cls.DECLENSIONS.get(nominative, {}).get('abl')


class Tokenizer:
    """Tokenize LATIN source code."""
    
    KEYWORDS = ['SIT', 'EST', 'SI', 'FINIS', 'SCRIBE', 'ADDE', 'DEME', 'AEQUAT']
    
    def __init__(self, declared_vars: set):
        self.declared_vars = declared_vars
    
    def tokenize_line(self, line: str) -> List[Tuple[str, str]]:
        """
        Tokenize a single line of LATIN code.
        Returns list of (token_type, value) tuples.
        """
        # Remove comments
        if ';' in line:
            line = line.split(';')[0]
        
        line = line.strip()
        if not line:
            return []
        
        tokens = []
        pos = 0
        
        while pos < len(line):
            matched = False
            
            # Try to match keywords
            for keyword in self.KEYWORDS:
                if line[pos:].startswith(keyword):
                    tokens.append(('KEYWORD', keyword))
                    pos += len(keyword)
                    matched = True
                    break
            
            if matched:
                # Special handling for SIT - next token is a new variable name
                if tokens[-1] == ('KEYWORD', 'SIT'):
                    # Look for a valid Latin noun in the remaining text
                    remaining = line[pos:]
                    found_var = None
                    for nom in LatinDeclension.DECLENSIONS.keys():
                        if remaining.startswith(nom):
                            found_var = nom
                            break
                    
                    if found_var:
                        tokens.append(('VARIABLE', found_var))
                        pos += len(found_var)
                        continue
                
                continue
            
            # Try to match Roman numerals (greedy)
            roman_match = ''
            temp_pos = pos
            while temp_pos < len(line) and line[temp_pos] in 'MDCLXVI':
                roman_match += line[temp_pos]
                temp_pos += 1
            
            if roman_match:
                num = RomanNumeralParser.parse(roman_match)
                if num is not None:
                    tokens.append(('NUMBER', num))
                    pos = temp_pos
                    continue
            
            # Try to match variable names (longest match)
            best_match = None
            best_length = 0
            
            for var in self.declared_vars:
                # Check nominative
                if line[pos:].startswith(var):
                    if len(var) > best_length:
                        best_match = ('VARIABLE', var)
                        best_length = len(var)
                
                # Check accusative
                acc = LatinDeclension.get_accusative(var)
                if acc and line[pos:].startswith(acc):
                    if len(acc) > best_length:
                        best_match = ('VARIABLE', var)
                        best_length = len(acc)
                
                # Check dative
                dat = LatinDeclension.get_dative(var)
                if dat and line[pos:].startswith(dat):
                    if len(dat) > best_length:
                        best_match = ('VARIABLE', var)
                        best_length = len(dat)
                
                # Check ablative
                abl = LatinDeclension.get_ablative(var)
                if abl and line[pos:].startswith(abl):
                    if len(abl) > best_length:
                        best_match = ('VARIABLE', var)
                        best_length = len(abl)
            
            if best_match:
                tokens.append(best_match)
                pos += best_length
                continue
            
            # Unknown token - error
            raise RuntimeError(f"ERRATUM: '{line[pos:]}' non intellegitur")
        
        return tokens


class LatinInterpreter:
    """Interpret and execute LATIN programs."""
    
    def __init__(self):
        self.variables: Dict[str, int] = {}
        self.declared_vars: set = set()
        self.tokenizer = Tokenizer(self.declared_vars)
        self.in_conditional = False
        self.skip_execution = False
    
    def run(self, source: str):
        """Execute LATIN source code."""
        lines = source.split('\n')
        i = 0
        
        while i < len(lines):
            line = lines[i].strip()
            
            # Skip empty lines and comments
            if not line or line.startswith(';'):
                i += 1
                continue
            
            try:
                self.execute_line(line)
            except Exception as e:
                print(f"Error on line {i + 1}: {e}", file=sys.stderr)
                sys.exit(1)
            
            i += 1
    
    def execute_line(self, line: str):
        """Execute a single line of LATIN code."""
        tokens = self.tokenizer.tokenize_line(line)
        
        if not tokens:
            return
        
        # Handle FINIS (end conditional block)
        if tokens[0] == ('KEYWORD', 'FINIS'):
            self.in_conditional = False
            self.skip_execution = False
            return
        
        # Skip execution if in false conditional
        if self.skip_execution:
            return
        
        # Handle SIT (variable declaration)
        if tokens[0] == ('KEYWORD', 'SIT'):
            if len(tokens) != 2 or tokens[1][0] != 'VARIABLE':
                raise RuntimeError("ERRATUM: Syntax incorrecta post SIT")
            var_name = tokens[1][1]
            self.declared_vars.add(var_name)
            self.variables[var_name] = 0
            return
        
        # Handle SCRIBE (print)
        if tokens[0] == ('KEYWORD', 'SCRIBE'):
            if len(tokens) != 2:
                raise RuntimeError("ERRATUM: Syntax incorrecta post SCRIBE")
            if tokens[1][0] == 'NUMBER':
                print(tokens[1][1])
            elif tokens[1][0] == 'VARIABLE':
                var_name = tokens[1][1]
                if var_name not in self.variables:
                    raise RuntimeError(f"ERRATUM: '{var_name}' non declaratur")
                print(self.variables[var_name])
            return
        
        # Handle SI (conditional)
        if tokens[0] == ('KEYWORD', 'SI'):
            # Parse: SI VARIABLE AEQUAT NUMBER/VARIABLE
            if len(tokens) != 4:
                raise RuntimeError("ERRATUM: Syntax incorrecta in SI")
            if tokens[1][0] != 'VARIABLE':
                raise RuntimeError("ERRATUM: SI requirit variabilem")
            if tokens[2] != ('KEYWORD', 'AEQUAT'):
                raise RuntimeError("ERRATUM: SI requirit AEQUAT")
            
            var_name = tokens[1][1]
            if var_name not in self.variables:
                raise RuntimeError(f"ERRATUM: '{var_name}' non declaratur")
            
            left_value = self.variables[var_name]
            
            if tokens[3][0] == 'NUMBER':
                right_value = tokens[3][1]
            elif tokens[3][0] == 'VARIABLE':
                right_var = tokens[3][1]
                if right_var not in self.variables:
                    raise RuntimeError(f"ERRATUM: '{right_var}' non declaratur")
                right_value = self.variables[right_var]
            else:
                raise RuntimeError("ERRATUM: SI requirit numerum aut variabilem")
            
            self.in_conditional = True
            self.skip_execution = (left_value != right_value)
            return
        
        # Handle assignment (VARIABLE EST ...)
        if len(tokens) >= 3 and tokens[0][0] == 'VARIABLE' and tokens[1] == ('KEYWORD', 'EST'):
            var_name = tokens[0][1]
            if var_name not in self.variables:
                raise RuntimeError(f"ERRATUM: '{var_name}' non declaratur")
            
            # Simple assignment: VARIABLE EST NUMBER
            if len(tokens) == 3 and tokens[2][0] == 'NUMBER':
                self.variables[var_name] = tokens[2][1]
                return
            
            # VARIABLE EST VARIABLE
            if len(tokens) == 3 and tokens[2][0] == 'VARIABLE':
                source_var = tokens[2][1]
                if source_var not in self.variables:
                    raise RuntimeError(f"ERRATUM: '{source_var}' non declaratur")
                self.variables[var_name] = self.variables[source_var]
                return
            
            # VARIABLE EST ADDE ...
            if len(tokens) >= 4 and tokens[2] == ('KEYWORD', 'ADDE'):
                result = self.evaluate_addition(tokens[3:])
                self.variables[var_name] = result
                return
            
            # VARIABLE EST DEME ...
            if len(tokens) >= 4 and tokens[2] == ('KEYWORD', 'DEME'):
                result = self.evaluate_subtraction(tokens[3:])
                self.variables[var_name] = result
                return
            
            raise RuntimeError("ERRATUM: Syntax incorrecta in assignatione")
        
        raise RuntimeError("ERRATUM: Syntax non cognita")
    
    def evaluate_addition(self, tokens: List[Tuple[str, str]]) -> int:
        """Evaluate ADDE operation."""
        if len(tokens) != 2:
            raise RuntimeError("ERRATUM: ADDE requirit duos operandos")
        
        values = []
        for token_type, token_value in tokens:
            if token_type == 'NUMBER':
                values.append(token_value)
            elif token_type == 'VARIABLE':
                if token_value not in self.variables:
                    raise RuntimeError(f"ERRATUM: '{token_value}' non declaratur")
                values.append(self.variables[token_value])
            else:
                raise RuntimeError("ERRATUM: ADDE requirit numeros aut variabiles")
        
        return values[0] + values[1]
    
    def evaluate_subtraction(self, tokens: List[Tuple[str, str]]) -> int:
        """Evaluate DEME operation."""
        if len(tokens) != 2:
            raise RuntimeError("ERRATUM: DEME requirit duos operandos")
        
        values = []
        for token_type, token_value in tokens:
            if token_type == 'NUMBER':
                values.append(token_value)
            elif token_type == 'VARIABLE':
                if token_value not in self.variables:
                    raise RuntimeError(f"ERRATUM: '{token_value}' non declaratur")
                values.append(self.variables[token_value])
            else:
                raise RuntimeError("ERRATUM: DEME requirit numeros aut variabiles")
        
        return values[0] - values[1]


def main():
    """Main entry point for the LATIN interpreter."""
    if len(sys.argv) < 2:
        print("Usage: latin.py <file.lat>")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    try:
        with open(filename, 'r') as f:
            source = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found", file=sys.stderr)
        sys.exit(1)
    
    interpreter = LatinInterpreter()
    interpreter.run(source)


if __name__ == '__main__':
    main()
