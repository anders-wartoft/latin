#!/usr/bin/env python3
"""
LATIN Interpreter - Enhanced Version
Latin Ain't This Insufferable Normally
Full-featured interpreter with loops, functions, and more arithmetic.
"""

import re
import sys
from typing import Dict, List, Optional, Tuple


class RomanNumeralParser:
    """Parse Roman numerals to integers and vice versa."""
    
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
    
    @classmethod
    def to_roman(cls, num: int) -> str:
        """Convert an integer to Roman numeral string."""
        if num <= 0:
            return "NIHIL"  # "nothing" in Latin
        
        values = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        result = []
        for value, numeral in values:
            count = num // value
            if count:
                result.append(numeral * count)
                num -= value * count
        
        return ''.join(result)


class LatinDeclension:
    """Handle Latin noun declensions."""
    
    # Expanded declension table
    DECLENSIONS = {
        # Second declension masculine
        'NUMERUS': {'acc': 'NUMERUM', 'dat': 'NUMERO', 'abl': 'NUMERO'},
        'PRIMUS': {'acc': 'PRIMUM', 'dat': 'PRIMO', 'abl': 'PRIMO'},
        'SECUNDUS': {'acc': 'SECUNDUM', 'dat': 'SECUNDO', 'abl': 'SECUNDO'},
        'TERTIUS': {'acc': 'TERTIUM', 'dat': 'TERTIO', 'abl': 'TERTIO'},
        'QUARTUS': {'acc': 'QUARTUM', 'dat': 'QUARTO', 'abl': 'QUARTO'},
        'QUINTUS': {'acc': 'QUINTUM', 'dat': 'QUINTO', 'abl': 'QUINTO'},
        'MAXIMVS': {'acc': 'MAXIMVM', 'dat': 'MAXIMO', 'abl': 'MAXIMO'},
        'AMICUS': {'acc': 'AMICUM', 'dat': 'AMICO', 'abl': 'AMICO'},
        'SERVUS': {'acc': 'SERVUM', 'dat': 'SERVO', 'abl': 'SERVO'},
        'DOMINUS': {'acc': 'DOMINUM', 'dat': 'DOMINO', 'abl': 'DOMINO'},
        'FILIUS': {'acc': 'FILIUM', 'dat': 'FILIO', 'abl': 'FILIO'},
        'ANNUS': {'acc': 'ANNUM', 'dat': 'ANNO', 'abl': 'ANNO'},
        'LIBER': {'acc': 'LIBRUM', 'dat': 'LIBRO', 'abl': 'LIBRO'},
        'VENTER': {'acc': 'VENTREM', 'dat': 'VENTRI', 'abl': 'VENTRE'},
        'INDEX': {'acc': 'INDICEM', 'dat': 'INDICI', 'abl': 'INDICE'},
        'RESULTAT': {'acc': 'RESULTATUM', 'dat': 'RESULTATO', 'abl': 'RESULTATO'},
        # Second declension neuter
        'BELLVM': {'acc': 'BELLVM', 'dat': 'BELLO', 'abl': 'BELLO'},
        'VERBVM': {'acc': 'VERBVM', 'dat': 'VERBO', 'abl': 'VERBO'},
        'DONVM': {'acc': 'DONVM', 'dat': 'DONO', 'abl': 'DONO'},
        'PRAEFIXVM': {'acc': 'PRAEFIXVM', 'dat': 'PRAEFIXO', 'abl': 'PRAEFIXO'},
        # First declension feminine
        'PUELLA': {'acc': 'PUELLAM', 'dat': 'PUELLAE', 'abl': 'PUELLA'},
        'ROSA': {'acc': 'ROSAM', 'dat': 'ROSAE', 'abl': 'ROSA'},
        'AQUA': {'acc': 'AQUAM', 'dat': 'AQUAE', 'abl': 'AQUA'},
        'VITA': {'acc': 'VITAM', 'dat': 'VITAE', 'abl': 'VITA'},
        'TERRA': {'acc': 'TERRAM', 'dat': 'TERRAE', 'abl': 'TERRA'},
        'SUMMA': {'acc': 'SUMMAM', 'dat': 'SUMMAE', 'abl': 'SUMMA'},
        # Third declension
        'REX': {'acc': 'REGEM', 'dat': 'REGI', 'abl': 'REGE'},
        'CIVIS': {'acc': 'CIVEM', 'dat': 'CIVI', 'abl': 'CIVE'},
        'CORPVS': {'acc': 'CORPVS', 'dat': 'CORPORI', 'abl': 'CORPORE'},
        'TEMPVS': {'acc': 'TEMPVS', 'dat': 'TEMPORI', 'abl': 'TEMPORE'},
        'ITER': {'acc': 'ITER', 'dat': 'ITINERI', 'abl': 'ITINERE'},
        'NOMEN': {'acc': 'NOMEN', 'dat': 'NOMINI', 'abl': 'NOMINE'},
        'AETAS': {'acc': 'AETATEM', 'dat': 'AETATI', 'abl': 'AETATE'},
        'SALVTATIO': {'acc': 'SALVTATIONEM', 'dat': 'SALVTATIONI', 'abl': 'SALVTATIONE'},
        # Fourth declension
        'MANVS': {'acc': 'MANVM', 'dat': 'MANVI', 'abl': 'MANV'},
        'GRADVS': {'acc': 'GRADVM', 'dat': 'GRADVI', 'abl': 'GRADV'},
        # Fifth declension
        'RES': {'acc': 'REM', 'dat': 'REI', 'abl': 'RE'},
        'DIES': {'acc': 'DIEM', 'dat': 'DIEI', 'abl': 'DIE'},
    }
    
    @classmethod
    def get_nominative(cls, declined_form: str) -> Optional[str]:
        """Get the nominative form of a declined noun."""
        if declined_form in cls.DECLENSIONS:
            return declined_form
        
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
    
    KEYWORDS = ['SIT', 'EST', 'SI', 'ALITER', 'FINIS', 'SCRIBE', 'LEGO', 'ADDE', 'DEME', 'AEQUAT', 
                'DUM', 'FAC', 'REDDO', 'DVCE', 'MVLTIPLICA', 'MAIVS', 'MINOR', 'IVNGE',
                'INCIPITCVM', 'FINITVRCVM', 'CONTINET', 'INDICEDE']
    
    def __init__(self, declared_vars: set):
        self.declared_vars = declared_vars
    
    def tokenize_line(self, line: str) -> List[Tuple[str, str]]:
        """Tokenize a single line of LATIN code."""
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
            
            # Try to match string literals (quoted text)
            if line[pos] == '"':
                end_quote = line.find('"', pos + 1)
                if end_quote == -1:
                    raise RuntimeError(f"ERRATUM: unclosed string literal")
                string_content = line[pos + 1:end_quote]
                tokens.append(('STRING', string_content))
                pos = end_quote + 1
                continue
            
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
            
            # Try to match NIHIL (zero)
            if line[pos:].startswith('NIHIL'):
                tokens.append(('NUMBER', 0))
                pos += 5
                continue
            
            # Try to match variable names first (to avoid M in MAXIMVS being parsed as 1000)
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
                # Check if next token would be a keyword - if so, prefer shorter variable match
                remaining_after = line[pos + best_length:]
                keyword_after = any(remaining_after.startswith(kw) for kw in self.KEYWORDS)
                
                if not keyword_after and best_length > 0:
                    # Try shorter matches to see if they would allow a keyword
                    var_name = best_match[1]
                    nom_len = len(var_name)
                    
                    # If we matched a declined form, check if nominative + keyword would work
                    if best_length > nom_len and line[pos:].startswith(var_name):
                        remaining_with_nom = line[pos + nom_len:]
                        if any(remaining_with_nom.startswith(kw) for kw in self.KEYWORDS):
                            # Use nominative match instead
                            best_length = nom_len
                
                tokens.append(best_match)
                pos += best_length
                continue
            
            # Try to match Roman numerals (only if no variable matched)
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
            
            # Unknown token - error
            raise RuntimeError(f"ERRATUM: '{line[pos:]}' non intellegitur")
        
        return tokens


class LatinInterpreter:
    """Interpret and execute LATIN programs."""
    
    def __init__(self, use_english_errors=False):
        self.variables: Dict[str, any] = {}  # Can hold int or str
        self.declared_vars: set = set()
        self.tokenizer = Tokenizer(self.declared_vars)
        self.skip_execution = False
        self.use_english_errors = use_english_errors
        self.lines = []
        self.line_index = 0
        self.loop_starts = []  # Stack of loop start line numbers
    
    def error(self, latin_msg: str, english_msg: str):
        """Raise error in Latin or English based on settings."""
        if self.use_english_errors:
            raise RuntimeError(english_msg)
        else:
            raise RuntimeError(f"ERRATUM: {latin_msg}")
    
    def run(self, source: str):
        """Execute LATIN source code."""
        self.lines = source.split('\n')
        self.line_index = 0
        
        while self.line_index < len(self.lines):
            line = self.lines[self.line_index].strip()
            
            # Remove inline comments
            if ';' in line:
                line = line.split(';')[0].strip()
            
            # Skip empty lines
            if not line:
                self.line_index += 1
                continue
            
            try:
                jump = self.execute_line(line)
                if jump is not None:
                    self.line_index = jump
                else:
                    self.line_index += 1
            except Exception as e:
                print(f"Error on line {self.line_index + 1}: {e}", file=sys.stderr)
                sys.exit(1)
    
    def execute_line(self, line: str) -> Optional[int]:
        """Execute a single line. Returns new line number if jump, else None."""
        tokens = self.tokenizer.tokenize_line(line)
        
        if not tokens:
            return None
        
        # Handle FINIS (end block)
        if tokens[0] == ('KEYWORD', 'FINIS'):
            self.skip_execution = False
            # If this ends a loop, jump back to loop start
            if self.loop_starts:
                loop_start = self.loop_starts.pop()
                return loop_start
            return None
        
        # Skip execution if in false conditional or loop condition
        if self.skip_execution:
            return None
        
        # Handle SIT (variable declaration)
        if tokens[0] == ('KEYWORD', 'SIT'):
            if len(tokens) != 2 or tokens[1][0] != 'VARIABLE':
                self.error("Syntax incorrecta post SIT", "Invalid syntax after SIT")
            var_name = tokens[1][1]
            self.declared_vars.add(var_name)
            self.variables[var_name] = 0  # Default to 0 for compatibility
            return None
        
        # Handle SCRIBE (print)
        if tokens[0] == ('KEYWORD', 'SCRIBE'):
            if len(tokens) != 2:
                self.error("Syntax incorrecta post SCRIBE", "Invalid syntax after SCRIBE")
            if tokens[1][0] == 'STRING':
                print(tokens[1][1])
            elif tokens[1][0] == 'NUMBER':
                print(RomanNumeralParser.to_roman(tokens[1][1]))
            elif tokens[1][0] == 'VARIABLE':
                var_name = tokens[1][1]
                if var_name not in self.variables:
                    self.error(f"'{var_name}' non declaratur", f"Variable '{var_name}' not declared")
                value = self.variables[var_name]
                if isinstance(value, int):
                    print(RomanNumeralParser.to_roman(value))
                else:
                    print(value)
            return None
        
        # Handle LEGO (read input)
        if tokens[0] == ('KEYWORD', 'LEGO'):
            if len(tokens) != 2:
                self.error("Syntax incorrecta post LEGO", "Invalid syntax after LEGO")
            if tokens[1][0] != 'VARIABLE':
                self.error("LEGO requirit variabilem", "LEGO requires a variable")
            
            var_name = tokens[1][1]
            if var_name not in self.variables:
                self.error(f"'{var_name}' non declaratur", f"Variable '{var_name}' not declared")
            
            # Read input from user
            user_input = input().strip()
            
            # Try to parse as Roman numeral first
            value = RomanNumeralParser.parse(user_input)
            if value is not None:
                self.variables[var_name] = value
            else:
                # If not a valid Roman numeral, treat as string
                # Remove quotes if user included them
                if user_input.startswith('"') and user_input.endswith('"'):
                    user_input = user_input[1:-1]
                self.variables[var_name] = user_input
            
            return None
        
        # Handle DUM (while loop)
        if tokens[0] == ('KEYWORD', 'DUM'):
            # DUM VARIABLE COMPARISON VALUE
            if len(tokens) != 4:
                self.error("Syntax incorrecta in DUM", "Invalid DUM syntax")
            if tokens[1][0] != 'VARIABLE':
                self.error("DUM requirit variabilem", "DUM requires variable")
            if tokens[2][1] not in ['AEQUAT', 'MAIVS', 'MINOR']:
                self.error("DUM requirit AEQUAT, MAIVS, aut MINOR", "DUM requires AEQUAT, MAIVS, or MINOR")
            
            var_name = tokens[1][1]
            if var_name not in self.variables:
                self.error(f"'{var_name}' non declaratur", f"Variable '{var_name}' not declared")
            
            left_value = self.variables[var_name]
            
            if tokens[3][0] == 'NUMBER':
                right_value = tokens[3][1]
            elif tokens[3][0] == 'VARIABLE':
                right_var = tokens[3][1]
                if right_var not in self.variables:
                    self.error(f"'{right_var}' non declaratur", f"Variable '{right_var}' not declared")
                right_value = self.variables[right_var]
            else:
                self.error("DUM requirit numerum aut variabilem", "DUM requires number or variable")
            
            # Evaluate condition
            condition_met = False
            if tokens[2][1] == 'AEQUAT':
                condition_met = (left_value == right_value)
            elif tokens[2][1] == 'MAIVS':
                condition_met = (left_value > right_value)
            elif tokens[2][1] == 'MINOR':
                condition_met = (left_value < right_value)
            
            # If condition is false, skip to FINIS
            if not condition_met:
                depth = 1
                search_idx = self.line_index + 1
                while search_idx < len(self.lines) and depth > 0:
                    search_line = self.lines[search_idx].strip()
                    if ';' in search_line:
                        search_line = search_line.split(';')[0].strip()
                    if search_line.startswith('DUM') or search_line.startswith('SI'):
                        depth += 1
                    elif search_line == 'FINIS':
                        depth -= 1
                    search_idx += 1
                return search_idx - 1
            # Otherwise continue into loop and remember start position
            self.loop_starts.append(self.line_index)
            return None
        
        # Handle ALITER (else)
        if tokens[0] == ('KEYWORD', 'ALITER'):
            # When we reach ALITER, it means the SI condition was true
            # So we need to skip to FINIS
            depth = 1
            search_idx = self.line_index + 1
            while search_idx < len(self.lines) and depth > 0:
                search_line = self.lines[search_idx].strip()
                if ';' in search_line:
                    search_line = search_line.split(';')[0].strip()
                if search_line.startswith('SI') or search_line.startswith('DUM'):
                    depth += 1
                elif search_line == 'FINIS':
                    depth -= 1
                search_idx += 1
            return search_idx - 1
        
        # Handle SI (conditional)
        if tokens[0] == ('KEYWORD', 'SI'):
            # Parse: SI VARIABLE AEQUAT NUMBER/VARIABLE/STRING
            # Or: SI VARIABLE MAIVS/MINOR NUMBER/VARIABLE
            if len(tokens) != 4:
                self.error("Syntax incorrecta in SI", "Invalid SI syntax")
            if tokens[1][0] != 'VARIABLE':
                self.error("SI requirit variabilem", "SI requires variable")
            if tokens[2][1] not in ['AEQUAT', 'MAIVS', 'MINOR']:
                self.error("SI requirit AEQUAT, MAIVS, aut MINOR", "SI requires AEQUAT, MAIVS, or MINOR")
            
            var_name = tokens[1][1]
            if var_name not in self.variables:
                self.error(f"'{var_name}' non declaratur", f"Variable '{var_name}' not declared")
            
            left_value = self.variables[var_name]
            
            if tokens[3][0] == 'STRING':
                right_value = tokens[3][1]
            elif tokens[3][0] == 'NUMBER':
                right_value = tokens[3][1]
            elif tokens[3][0] == 'VARIABLE':
                right_var = tokens[3][1]
                if right_var not in self.variables:
                    self.error(f"'{right_var}' non declaratur", f"Variable '{right_var}' not declared")
                right_value = self.variables[right_var]
            else:
                self.error("SI requirit numerum, textum, aut variabilem", "SI requires number, string, or variable")
            
            # Evaluate condition
            condition_met = False
            if tokens[2][1] == 'AEQUAT':
                condition_met = (left_value == right_value)
            elif tokens[2][1] == 'MAIVS':
                # Only works with numbers
                if not isinstance(left_value, int) or not isinstance(right_value, int):
                    self.error("MAIVS requirit numeros", "MAIVS requires numbers")
                condition_met = (left_value > right_value)
            elif tokens[2][1] == 'MINOR':
                # Only works with numbers
                if not isinstance(left_value, int) or not isinstance(right_value, int):
                    self.error("MINOR requirit numeros", "MINOR requires numbers")
                condition_met = (left_value < right_value)
            
            if not condition_met:
                # Skip to ALITER or FINIS
                depth = 1
                search_idx = self.line_index + 1
                while search_idx < len(self.lines) and depth > 0:
                    search_line = self.lines[search_idx].strip()
                    if ';' in search_line:
                        search_line = search_line.split(';')[0].strip()
                    if search_line.startswith('SI') or search_line.startswith('DUM'):
                        depth += 1
                    elif search_line == 'ALITER' and depth == 1:
                        # Found ALITER at same depth - jump past it to continue with else block
                        return search_idx + 1
                    elif search_line == 'FINIS':
                        depth -= 1
                    search_idx += 1
                return search_idx - 1
            return None
        
        # Handle assignment (VARIABLE EST ...)
        if len(tokens) >= 3 and tokens[0][0] == 'VARIABLE' and tokens[1] == ('KEYWORD', 'EST'):
            var_name = tokens[0][1]
            if var_name not in self.variables:
                self.error(f"'{var_name}' non declaratur", f"Variable '{var_name}' not declared")
            
            # Simple assignment: VARIABLE EST STRING
            if len(tokens) == 3 and tokens[2][0] == 'STRING':
                self.variables[var_name] = tokens[2][1]
                return None
            
            # Simple assignment: VARIABLE EST NUMBER
            if len(tokens) == 3 and tokens[2][0] == 'NUMBER':
                self.variables[var_name] = tokens[2][1]
                return None
            
            # VARIABLE EST VARIABLE
            if len(tokens) == 3 and tokens[2][0] == 'VARIABLE':
                source_var = tokens[2][1]
                if source_var not in self.variables:
                    self.error(f"'{source_var}' non declaratur", f"Variable '{source_var}' not declared")
                self.variables[var_name] = self.variables[source_var]
                return None
            
            # VARIABLE EST IVNGE ... (string concatenation)
            if len(tokens) >= 4 and tokens[2] == ('KEYWORD', 'IVNGE'):
                result = self.evaluate_concatenation(tokens[3:])
                self.variables[var_name] = result
                return None
            
            # VARIABLE EST INCIPITCVM ... (string startswith)
            if len(tokens) >= 4 and tokens[2] == ('KEYWORD', 'INCIPITCVM'):
                result = self.evaluate_string_operation('INCIPITCVM', tokens[3:])
                self.variables[var_name] = result
                return None
            
            # VARIABLE EST FINITVRCVM ... (string endswith)
            if len(tokens) >= 4 and tokens[2] == ('KEYWORD', 'FINITVRCVM'):
                result = self.evaluate_string_operation('FINITVRCVM', tokens[3:])
                self.variables[var_name] = result
                return None
            
            # VARIABLE EST CONTINET ... (string contains)
            if len(tokens) >= 4 and tokens[2] == ('KEYWORD', 'CONTINET'):
                result = self.evaluate_string_operation('CONTINET', tokens[3:])
                self.variables[var_name] = result
                return None
            
            # VARIABLE EST INDICEDE ... (string indexof)
            if len(tokens) >= 4 and tokens[2] == ('KEYWORD', 'INDICEDE'):
                result = self.evaluate_string_operation('INDICEDE', tokens[3:])
                self.variables[var_name] = result
                return None
            
            # VARIABLE EST ADDE ...
            if len(tokens) >= 4 and tokens[2] == ('KEYWORD', 'ADDE'):
                result = self.evaluate_operation('ADDE', tokens[3:])
                self.variables[var_name] = result
                return None
            
            # VARIABLE EST DEME ...
            if len(tokens) >= 4 and tokens[2] == ('KEYWORD', 'DEME'):
                result = self.evaluate_operation('DEME', tokens[3:])
                self.variables[var_name] = result
                return None
            
            # VARIABLE EST MVLTIPLICA ...
            if len(tokens) >= 4 and tokens[2] == ('KEYWORD', 'MVLTIPLICA'):
                result = self.evaluate_operation('MVLTIPLICA', tokens[3:])
                self.variables[var_name] = result
                return None
            
            # VARIABLE EST DVCE ...
            if len(tokens) >= 4 and tokens[2] == ('KEYWORD', 'DVCE'):
                result = self.evaluate_operation('DVCE', tokens[3:])
                self.variables[var_name] = result
                return None
            
            self.error("Syntax incorrecta in assignatione", "Invalid assignment syntax")
        
        self.error("Syntax non cognita", "Unknown syntax")
    
    def evaluate_concatenation(self, tokens: List[Tuple[str, str]]) -> str:
        """Evaluate string concatenation."""
        if len(tokens) != 2:
            self.error("IVNGE requirit duos operandos", "IVNGE requires two operands")
        
        values = []
        for token_type, token_value in tokens:
            if token_type == 'STRING':
                values.append(token_value)
            elif token_type == 'VARIABLE':
                if token_value not in self.variables:
                    self.error(f"'{token_value}' non declaratur", f"Variable '{token_value}' not declared")
                var_val = self.variables[token_value]
                if isinstance(var_val, int):
                    values.append(RomanNumeralParser.to_roman(var_val))
                else:
                    values.append(var_val)
            else:
                self.error("IVNGE requirit textum aut variabiles", "IVNGE requires strings or variables")
        
        return values[0] + values[1]
    
    def evaluate_string_operation(self, op: str, tokens: List[Tuple[str, str]]):
        """Evaluate string operations (startswith, endswith, contains, indexof)."""
        if len(tokens) != 2:
            self.error(f"{op} requirit duos operandos", f"{op} requires two operands")
        
        # Get string values
        values = []
        for token_type, token_value in tokens:
            if token_type == 'STRING':
                values.append(token_value)
            elif token_type == 'VARIABLE':
                if token_value not in self.variables:
                    self.error(f"'{token_value}' non declaratur", f"Variable '{token_value}' not declared")
                var_val = self.variables[token_value]
                if isinstance(var_val, int):
                    self.error(f"{op} requirit textum", f"{op} requires strings")
                values.append(var_val)
            else:
                self.error(f"{op} requirit textum aut variabiles", f"{op} requires strings or variables")
        
        str1, str2 = values[0], values[1]
        
        # Perform operation
        if op == 'INCIPITCVM':
            return 1 if str1.startswith(str2) else 0
        elif op == 'FINITVRCVM':
            return 1 if str1.endswith(str2) else 0
        elif op == 'CONTINET':
            return 1 if str2 in str1 else 0
        elif op == 'INDICEDE':
            idx = str1.find(str2)
            return idx if idx != -1 else 0  # Return 0 (NIHIL) if not found instead of -1
        
        return 0
    
    def evaluate_operation(self, op: str, tokens: List[Tuple[str, str]]) -> int:
        """Evaluate arithmetic operations."""
        if len(tokens) != 2:
            self.error(f"{op} requirit duos operandos", f"{op} requires two operands")
        
        values = []
        for token_type, token_value in tokens:
            if token_type == 'NUMBER':
                values.append(token_value)
            elif token_type == 'VARIABLE':
                if token_value not in self.variables:
                    self.error(f"'{token_value}' non declaratur", f"Variable '{token_value}' not declared")
                values.append(self.variables[token_value])
            else:
                self.error(f"{op} requirit numeros aut variabiles", f"{op} requires numbers or variables")
        
        if op == 'ADDE':
            return values[0] + values[1]
        elif op == 'DEME':
            return values[0] - values[1]
        elif op == 'MVLTIPLICA':
            return values[0] * values[1]
        elif op == 'DVCE':
            if values[1] == 0:
                self.error("Divisio per nihil", "Division by zero")
            return values[0] // values[1]
        
        return 0


def repl():
    """Interactive REPL for LATIN."""
    print("LATIN REPL - Latin Ain't This Insufferable Normally")
    print("Type 'VALE' to quit, 'ANGLICE' for English errors, 'LATINE' for Latin errors")
    print()
    
    interpreter = LatinInterpreter(use_english_errors=False)
    
    while True:
        try:
            line = input("LATIN> ").strip()
            
            if not line:
                continue
            
            if line in ['VALE', 'EXIT']:  # Support both, but don't document EXIT
                print("Vale! (Goodbye!)")
                break
            
            if line == 'ANGLICE':
                interpreter.use_english_errors = True
                print("Error messages in English")
                continue
            
            if line == 'LATINE':
                interpreter.use_english_errors = False
                print("Nuntii erroris Latine")
                continue
            
            # Execute single line
            interpreter.line_index = 0
            interpreter.lines = [line]
            interpreter.execute_line(line)
            
        except KeyboardInterrupt:
            print("\nVale!")
            break
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)


def main():
    """Main entry point for the LATIN interpreter."""
    if len(sys.argv) < 2:
        # No file provided, start REPL
        repl()
        return
    
    if sys.argv[1] == '--repl':
        repl()
        return
    
    filename = sys.argv[1]
    use_english = '--english' in sys.argv
    
    try:
        with open(filename, 'r') as f:
            source = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found", file=sys.stderr)
        sys.exit(1)
    
    interpreter = LatinInterpreter(use_english_errors=use_english)
    interpreter.run(source)


if __name__ == '__main__':
    main()
