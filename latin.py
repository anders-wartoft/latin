#!/usr/bin/env python3
"""
LATIN Interpreter - Enhanced Version
Latin Ain't This Insufferable Normally
Full-featured interpreter with loops, functions, and more arithmetic.
"""

import re
import sys
from typing import Dict, List, Optional, Tuple


class LatinExceptionThrown(Exception):
    """Raised when a LATIN exception should be thrown (e.g., division by zero)."""
    def __init__(self, handler_line: int):
        self.handler_line = handler_line
        super().__init__()


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
        'NUMERUS': {'gen': 'NUMERI', 'acc': 'NUMERUM', 'dat': 'NUMERO', 'abl': 'NUMERO', 'voc': 'NUMERE'},
        'PRIMUS': {'gen': 'PRIMI', 'acc': 'PRIMUM', 'dat': 'PRIMO', 'abl': 'PRIMO', 'voc': 'PRIME'},
        'SECUNDUS': {'gen': 'SECUNDI', 'acc': 'SECUNDUM', 'dat': 'SECUNDO', 'abl': 'SECUNDO', 'voc': 'SECUNDE'},
        'TERTIUS': {'gen': 'TERTII', 'acc': 'TERTIUM', 'dat': 'TERTIO', 'abl': 'TERTIO', 'voc': 'TERTIE'},
        'QUARTUS': {'gen': 'QUARTI', 'acc': 'QUARTUM', 'dat': 'QUARTO', 'abl': 'QUARTO', 'voc': 'QUARTE'},
        'QUINTUS': {'gen': 'QUINTI', 'acc': 'QUINTUM', 'dat': 'QUINTO', 'abl': 'QUINTO', 'voc': 'QUINTE'},
        'MAXIMVS': {'gen': 'MAXIMI', 'acc': 'MAXIMVM', 'dat': 'MAXIMO', 'abl': 'MAXIMO', 'voc': 'MAXIME'},
        'AMICUS': {'gen': 'AMICI', 'acc': 'AMICUM', 'dat': 'AMICO', 'abl': 'AMICO', 'voc': 'AMICE'},
        'SERVUS': {'gen': 'SERVII', 'acc': 'SERVUM', 'dat': 'SERVO', 'abl': 'SERVO', 'voc': 'SERVE'},
        'DOMINUS': {'gen': 'DOMINI', 'acc': 'DOMINUM', 'dat': 'DOMINO', 'abl': 'DOMINO', 'voc': 'DOMINE'},
        'FILIUS': {'gen': 'FILII', 'acc': 'FILIUM', 'dat': 'FILIO', 'abl': 'FILIO', 'voc': 'FILI'},
        'ANNUS': {'gen': 'ANNI', 'acc': 'ANNUM', 'dat': 'ANNO', 'abl': 'ANNO', 'voc': 'ANNE'},
        'LIBER': {'gen': 'LIBRI', 'acc': 'LIBRUM', 'dat': 'LIBRO', 'abl': 'LIBRO', 'voc': 'LIBER'},
        'VENTER': {'gen': 'VENTRIS', 'acc': 'VENTREM', 'dat': 'VENTRI', 'abl': 'VENTRE', 'voc': 'VENTER'},
        'INDEX': {'gen': 'INDICIS', 'acc': 'INDICEM', 'dat': 'INDICI', 'abl': 'INDICE', 'voc': 'INDEX'},
        'RESULTAT': {'gen': 'RESULTATI', 'acc': 'RESULTATUM', 'dat': 'RESULTATO', 'abl': 'RESULTATO', 'voc': 'RESULTAT'},
        'ERROR': {'gen': 'ERRORIS', 'acc': 'ERROREM', 'dat': 'ERRORI', 'abl': 'ERRORE', 'voc': 'ERROR'},
        'EXCEPTIO': {'gen': 'EXCEPTIONIS', 'acc': 'EXCEPTIONEM', 'dat': 'EXCEPTIONI', 'abl': 'EXCEPTIONE', 'voc': 'EXCEPTIO'},
        # Second declension neuter
        'BELLVM': {'gen': 'BELLI', 'acc': 'BELLVM', 'dat': 'BELLO', 'abl': 'BELLO', 'voc': 'BELLVM'},
        'VERBVM': {'gen': 'VERBI', 'acc': 'VERBVM', 'dat': 'VERBO', 'abl': 'VERBO', 'voc': 'VERBVM'},
        'DONVM': {'gen': 'DONI', 'acc': 'DONVM', 'dat': 'DONO', 'abl': 'DONO', 'voc': 'DONVM'},
        'PRAEFIXVM': {'gen': 'PRAEFIXI', 'acc': 'PRAEFIXVM', 'dat': 'PRAEFIXO', 'abl': 'PRAEFIXO', 'voc': 'PRAEFIXVM'},
        # First declension feminine
        'PUELLA': {'gen': 'PUELLAE', 'acc': 'PUELLAM', 'dat': 'PUELLAE', 'abl': 'PUELLA', 'voc': 'PUELLA'},
        'ROSA': {'gen': 'ROSAE', 'acc': 'ROSAM', 'dat': 'ROSAE', 'abl': 'ROSA', 'voc': 'ROSA'},
        'AQUA': {'gen': 'AQUAE', 'acc': 'AQUAM', 'dat': 'AQUAE', 'abl': 'AQUA', 'voc': 'AQUA'},
        'VITA': {'gen': 'VITAE', 'acc': 'VITAM', 'dat': 'VITAE', 'abl': 'VITA', 'voc': 'VITA'},
        'TERRA': {'gen': 'TERRAE', 'acc': 'TERRAM', 'dat': 'TERRAE', 'abl': 'TERRA', 'voc': 'TERRA'},
        'SUMMA': {'gen': 'SUMMAE', 'acc': 'SUMMAM', 'dat': 'SUMMAE', 'abl': 'SUMMA', 'voc': 'SUMMA'},
        # Third declension
        'REX': {'gen': 'REGIS', 'acc': 'REGEM', 'dat': 'REGI', 'abl': 'REGE', 'voc': 'REX'},
        'CIVIS': {'gen': 'CIVIS', 'acc': 'CIVEM', 'dat': 'CIVI', 'abl': 'CIVE', 'voc': 'CIVIS'},
        'CORPVS': {'gen': 'CORPORIS', 'acc': 'CORPVS', 'dat': 'CORPORI', 'abl': 'CORPORE', 'voc': 'CORPVS'},
        'TEMPVS': {'gen': 'TEMPORIS', 'acc': 'TEMPVS', 'dat': 'TEMPORI', 'abl': 'TEMPORE', 'voc': 'TEMPVS'},
        'ITER': {'gen': 'ITINERIS', 'acc': 'ITER', 'dat': 'ITINERI', 'abl': 'ITINERE', 'voc': 'ITER'},
        'NOMEN': {'gen': 'NOMINIS', 'acc': 'NOMEN', 'dat': 'NOMINI', 'abl': 'NOMINE', 'voc': 'NOMEN'},
        'AETAS': {'gen': 'AETATIS', 'acc': 'AETATEM', 'dat': 'AETATI', 'abl': 'AETATE', 'voc': 'AETAS'},
        'SALVTATIO': {'gen': 'SALVTATIONIS', 'acc': 'SALVTATIONEM', 'dat': 'SALVTATIONI', 'abl': 'SALVTATIONE', 'voc': 'SALVTATIO'},
        'INPUTVM': {'gen': 'INPUTI', 'acc': 'INPUTVM', 'dat': 'INPUTO', 'abl': 'INPUTO', 'voc': 'INPUTVM'},
        'CONTINVA': {'gen': 'CONTINVAE', 'acc': 'CONTINVAM', 'dat': 'CONTINVAE', 'abl': 'CONTINVA', 'voc': 'CONTINVA'},
        'RESPONSUM': {'gen': 'RESPONSI', 'acc': 'RESPONSUM', 'dat': 'RESPONSO', 'abl': 'RESPONSO', 'voc': 'RESPONSUM'},
        # Fourth declension
        'MANVS': {'gen': 'MANVS', 'acc': 'MANVM', 'dat': 'MANVI', 'abl': 'MANV', 'voc': 'MANVS'},
        'GRADVS': {'gen': 'GRADVS', 'acc': 'GRADVM', 'dat': 'GRADVI', 'abl': 'GRADV', 'voc': 'GRADVS'},
        # Fifth declension
        'RES': {'gen': 'REI', 'acc': 'REM', 'dat': 'REI', 'abl': 'RE', 'voc': 'RES'},
        'DIES': {'gen': 'DIEI', 'acc': 'DIEM', 'dat': 'DIEI', 'abl': 'DIE', 'voc': 'DIES'},
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
    
    @classmethod
    def get_vocative(cls, nominative: str) -> Optional[str]:
        """Get the vocative form of a noun."""
        return cls.DECLENSIONS.get(nominative, {}).get('voc')
    
    @classmethod
    def get_genitive(cls, nominative: str) -> Optional[str]:
        """Get the genitive form of a noun."""
        return cls.DECLENSIONS.get(nominative, {}).get('gen')


class Tokenizer:
    """Tokenize LATIN source code."""
    
    KEYWORDS = ['SIT', 'EST', 'SI', 'ALITER', 'FINIS', 'SCRIBE', 'LEGO', 'ADDE', 'DEME', 'AEQUAT', 
                'DUM', 'FAC', 'REDDO', 'VOCA', 'DVCE', 'MVLTIPLICA', 'MAIVS', 'MINOR', 'IVNGE',
                'INCIPITCVM', 'FINITVRCVM', 'CONTINET', 'INDICEDE', 'IACE', 'CAPE', 'AVDI', 'NOTA']
    
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
                    # First try to find in DECLENSIONS table
                    for nom in LatinDeclension.DECLENSIONS.keys():
                        if remaining.startswith(nom):
                            found_var = nom
                            break
                    
                    if found_var:
                        tokens.append(('VARIABLE', found_var))
                        pos += len(found_var)
                    else:
                        # Variable not in declensions - parse as uppercase letters
                        end = pos
                        while end < len(line) and line[end].isupper():
                            end += 1
                        if end > pos:
                            var_name = line[pos:end]
                            tokens.append(('VARIABLE', var_name))
                            pos = end
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
                
                # Check vocative
                voc = LatinDeclension.get_vocative(var)
                if voc and line[pos:].startswith(voc):
                    if len(voc) > best_length:
                        best_match = ('VARIABLE', var)
                        best_length = len(voc)
                
                # Check genitive (for field access like NOMENSERVII)
                gen = LatinDeclension.get_genitive(var)
                if gen and line[pos:].startswith(gen):
                    if len(gen) > best_length:
                        best_match = ('GENITIVE', var)  # Mark as genitive for field access
                        best_length = len(gen)
            
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
        self.loop_starts = []  # Stack of (loop_start_line, depth_at_loop_start) tuples
        self.block_depth = 0  # Current nesting depth of SI/DUM/ALITER blocks
        self.functions = {}  # {function_name: {'params': [], 'start_line': int, 'end_line': int}}
        self.call_stack = []  # Stack of return addresses and saved variables
        self.in_function_def = False  # Track if we're currently defining a function
        self.exception_handlers = []  # Stack of (exception_type, handler_line) tuples
        self.current_exception = None  # Currently thrown exception
        self.exception_throw_line = None  # Line where exception was thrown
        self.skip_handler_pop = False  # Don't pop handler when FINIS balances a skip
    
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
            except LatinExceptionThrown as e:
                # Exception thrown during execution (e.g., division by zero)
                # Jump to the handler
                self.line_index = e.handler_line
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
            self.block_depth -= 1
            
            # Pop exception handler if this closes a CAPE block (but not if we're just balancing a skip)
            if self.skip_handler_pop:
                # Just balancing a CAPE skip - don't pop handler
                self.skip_handler_pop = False
            elif self.exception_handlers and self.exception_handlers[-1][1] <= self.line_index:
                self.exception_handlers.pop()
                # If we just handled an exception, end execution (jump past all lines)
                if self.exception_throw_line is not None:
                    self.exception_throw_line = None
                    self.current_exception = None
                    return len(self.lines)  # Jump past end to terminate
            
            # If this ends a loop (depth returns to loop start depth), jump back
            if self.loop_starts and self.loop_starts[-1][1] == self.block_depth:
                loop_start, _ = self.loop_starts.pop()
                self.block_depth += 1  # Re-enter the loop
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
            
            # If variable not in DECLENSIONS, add it with automatic declension pattern
            if var_name not in LatinDeclension.DECLENSIONS:
                # Guess declension based on ending
                if var_name.endswith('US'):
                    # Second declension masculine like NUMERUS
                    root = var_name[:-2]
                    LatinDeclension.DECLENSIONS[var_name] = {
                        'gen': root + 'I',
                        'acc': root + 'UM',
                        'dat': root + 'O',
                        'abl': root + 'O',
                        'voc': root + 'E'
                    }
                elif var_name.endswith('OR'):
                    # Third declension like ADDITOR, ERROR
                    LatinDeclension.DECLENSIONS[var_name] = {
                        'gen': var_name + 'IS',
                        'acc': var_name + 'EM',
                        'dat': var_name + 'I',
                        'abl': var_name + 'E',
                        'voc': var_name
                    }
                elif var_name.endswith('IO'):
                    # Third declension like EXCEPTIO
                    LatinDeclension.DECLENSIONS[var_name] = {
                        'gen': var_name + 'NIS',
                        'acc': var_name + 'NEM',
                        'dat': var_name + 'NI',
                        'abl': var_name + 'NE',
                        'voc': var_name
                    }
                elif var_name.endswith('A'):
                    # First declension feminine like SUMMA
                    root = var_name[:-1]
                    LatinDeclension.DECLENSIONS[var_name] = {
                        'gen': root + 'AE',
                        'acc': root + 'AM',
                        'dat': root + 'AE',
                        'abl': root + 'A',
                        'voc': root + 'A'
                    }
                elif var_name.endswith('VM') or var_name.endswith('UM'):
                    # Second declension neuter
                    root = var_name[:-2]
                    LatinDeclension.DECLENSIONS[var_name] = {
                        'gen': root + 'I',
                        'acc': var_name,
                        'dat': root + 'O',
                        'abl': root + 'O',
                        'voc': var_name
                    }
                else:
                    # Default to second declension masculine pattern
                    LatinDeclension.DECLENSIONS[var_name] = {
                        'gen': var_name + 'I',
                        'acc': var_name + 'M',
                        'dat': var_name + 'O',
                        'abl': var_name + 'O',
                        'voc': var_name + 'E'
                    }
            
            return None
        
        # Handle SCRIBE (print)
        if tokens[0] == ('KEYWORD', 'SCRIBE'):
            # SCRIBE FIELDGENITIVE (print field of object)
            if len(tokens) == 3 and tokens[1][0] == 'VARIABLE' and tokens[2][0] == 'GENITIVE':
                field_name = tokens[1][1]
                object_name = tokens[2][1]
                if object_name not in self.variables:
                    self.error(f"'{object_name}' non declaratur", f"Object '{object_name}' not declared")
                if not isinstance(self.variables[object_name], dict):
                    self.error(f"'{object_name}' non est structura", f"'{object_name}' is not a struct")
                if field_name not in self.variables[object_name]:
                    self.error(f"Campus '{field_name}' in '{object_name}' non existit", 
                              f"Field '{field_name}' in '{object_name}' does not exist")
                value = self.variables[object_name][field_name]
                if isinstance(value, int):
                    print(RomanNumeralParser.to_roman(value))
                else:
                    print(value)
                return None
                
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
        
        # Handle AVDI (debug print - with DEBUG prefix)
        if tokens[0] == ('KEYWORD', 'AVDI'):
            if len(tokens) != 2:
                self.error("Syntax incorrecta post AVDI", "Invalid syntax after AVDI")
            print("[DEBUG] ", end="", file=sys.stderr)
            if tokens[1][0] == 'STRING':
                print(tokens[1][1], file=sys.stderr)
            elif tokens[1][0] == 'NUMBER':
                print(RomanNumeralParser.to_roman(tokens[1][1]), file=sys.stderr)
            elif tokens[1][0] == 'VARIABLE':
                var_name = tokens[1][1]
                if var_name not in self.variables:
                    self.error(f"'{var_name}' non declaratur", f"Variable '{var_name}' not declared")
                value = self.variables[var_name]
                if isinstance(value, int):
                    print(RomanNumeralParser.to_roman(value), file=sys.stderr)
                else:
                    print(value, file=sys.stderr)
            return None
        
        # Handle NOTA (log print - with LOG prefix)
        if tokens[0] == ('KEYWORD', 'NOTA'):
            if len(tokens) != 2:
                self.error("Syntax incorrecta post NOTA", "Invalid syntax after NOTA")
            print("[LOG] ", end="", file=sys.stderr)
            if tokens[1][0] == 'STRING':
                print(tokens[1][1], file=sys.stderr)
            elif tokens[1][0] == 'NUMBER':
                print(RomanNumeralParser.to_roman(tokens[1][1]), file=sys.stderr)
            elif tokens[1][0] == 'VARIABLE':
                var_name = tokens[1][1]
                if var_name not in self.variables:
                    self.error(f"'{var_name}' non declaratur", f"Variable '{var_name}' not declared")
                value = self.variables[var_name]
                if isinstance(value, int):
                    print(RomanNumeralParser.to_roman(value), file=sys.stderr)
                else:
                    print(value, file=sys.stderr)
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
        
        # Handle IACE (throw exception)
        if tokens[0] == ('KEYWORD', 'IACE'):
            # IACE ERROR "message" or IACE ERROR
            if len(tokens) < 2:
                self.error("IACE requirit nomen exceptionis", "IACE requires exception name")
            if tokens[1][0] != 'VARIABLE':
                self.error("IACE requirit nomen exceptionis in vocativo", "IACE requires exception name in vocative")
            
            exception_name = tokens[1][1]
            message = ""
            if len(tokens) == 3 and tokens[2][0] == 'STRING':
                message = tokens[2][1]
            
            # Store exception info and throw line
            self.current_exception = {'type': exception_name, 'message': message}
            self.exception_throw_line = self.line_index + 1  # Continue after this line when done handling
            
            # Look for exception handler
            for handler_type, handler_line in reversed(self.exception_handlers):
                if handler_type == exception_name:
                    # Jump to handler
                    return handler_line
            
            # No handler found - raise error
            if message:
                self.error(f"{exception_name}: {message}", f"{exception_name}: {message}")
            else:
                self.error(exception_name, exception_name)
            
            return None
        
        # Handle CAPE (catch exception)
        if tokens[0] == ('KEYWORD', 'CAPE'):
            # CAPE ERROR
            if len(tokens) != 2:
                self.error("CAPE requirit nomen exceptionis", "CAPE requires exception name")
            if tokens[1][0] != 'VARIABLE':
                self.error("CAPE requirit nomen exceptionis in vocativo", "CAPE requires exception name in vocative")
            
            exception_name = tokens[1][1]
            
            # Register exception handler (will be active until FINIS)
            self.exception_handlers.append((exception_name, self.line_index + 1))
            self.block_depth += 1
            
            # If we're entering the handler after an exception, clear it
            if self.current_exception and self.current_exception['type'] == exception_name:
                self.current_exception = None
            else:
                # Not handling an exception now, skip to FINIS
                depth = 1
                search_idx = self.line_index + 1
                while search_idx < len(self.lines) and depth > 0:
                    search_line = self.lines[search_idx].strip()
                    if ';' in search_line:
                        search_line = search_line.split(';')[0].strip()
                    if search_line.startswith('CAPE') or search_line.startswith('SI') or search_line.startswith('DUM'):
                        depth += 1
                    elif search_line == 'FINIS':
                        depth -= 1
                    search_idx += 1
                # Balance for FINIS
                self.block_depth += 1
                self.skip_handler_pop = True  # Don't pop handler, we want it to stay active
                return search_idx - 1
            
            return None
        
        # Handle FAC (function definition)
        if tokens[0] == ('KEYWORD', 'FAC'):
            # FAC FUNCTION_NAME PARAM1 PARAM2 ...
            if len(tokens) < 2:
                self.error("FAC requirit nomen functionis", "FAC requires function name")
            if tokens[1][0] != 'VARIABLE':
                self.error("FAC requirit nomen functionis validum", "FAC requires valid function name")
            
            func_name = tokens[1][1]
            params = []
            
            # Collect parameters (all should be variables in dative case)
            for i in range(2, len(tokens)):
                if tokens[i][0] != 'VARIABLE':
                    self.error("Parametri debent esse variabiles", "Parameters must be variables")
                params.append(tokens[i][1])
            
            # Find the matching FINIS for this function
            depth = 1
            search_idx = self.line_index + 1
            while search_idx < len(self.lines) and depth > 0:
                search_line = self.lines[search_idx].strip()
                if ';' in search_line:
                    search_line = search_line.split(';')[0].strip()
                if search_line.startswith('FAC') or search_line.startswith('SI') or search_line.startswith('DUM'):
                    depth += 1
                elif search_line == 'FINIS':
                    depth -= 1
                search_idx += 1
            
            # Store function definition
            self.functions[func_name] = {
                'params': params,
                'start_line': self.line_index + 1,
                'end_line': search_idx - 2  # -2 because search_idx is after FINIS
            }
            
            # Skip to FINIS (don't execute function body during definition)
            self.block_depth += 1  # Balance for FINIS
            return search_idx - 1
        
        # Handle REDDO (return from function)
        if tokens[0] == ('KEYWORD', 'REDDO'):
            if len(tokens) != 2:
                self.error("REDDO requirit valorem", "REDDO requires a value")
            
            # Get return value
            if tokens[1][0] == 'NUMBER':
                return_value = tokens[1][1]
            elif tokens[1][0] == 'STRING':
                return_value = tokens[1][1]
            elif tokens[1][0] == 'VARIABLE':
                var_name = tokens[1][1]
                if var_name not in self.variables:
                    self.error(f"'{var_name}' non declaratur", f"Variable '{var_name}' not declared")
                return_value = self.variables[var_name]
            else:
                self.error("REDDO requirit numerum, textum, aut variabilem", "REDDO requires number, string, or variable")
            
            # Pop call stack and restore context
            if not self.call_stack:
                self.error("REDDO extra functionem", "REDDO outside function")
            
            call_info = self.call_stack.pop()
            return_line = call_info['return_line']
            saved_vars = call_info['saved_vars']
            
            # If there was a calling variable, assign the return value to it
            calling_var = self.variables.get('__CALLING_VAR__')
            
            # Restore variables (remove local params, restore globals)
            self.variables = saved_vars.copy()
            
            # Assign return value to calling variable
            if calling_var:
                self.variables[calling_var] = return_value
            
            # Jump back to caller (next line after the call)
            return return_line + 1
        
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
            # Otherwise continue into loop and remember start position with current depth
            self.loop_starts.append((self.line_index, self.block_depth))
            self.block_depth += 1
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
                # Skip to ALITER or FINIS (don't change depth since we're not entering the block)
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
                        # Increment block_depth since we're entering the ALITER block
                        self.block_depth += 1
                        return search_idx + 1
                    elif search_line == 'FINIS':
                        depth -= 1
                    search_idx += 1
                # Jumped to FINIS - it will handle decrementing depth, so pre-increment to balance
                self.block_depth += 1
                return search_idx - 1
            # Condition is true, enter SI block
            self.block_depth += 1
            return None
        
        # Handle field assignment (FIELDGENITIVE EST ...)
        # Example: NOMENSERVII EST "Marcus" (name of servant is Marcus)
        if len(tokens) >= 3 and tokens[0][0] == 'VARIABLE' and tokens[1][0] == 'GENITIVE' and tokens[2] == ('KEYWORD', 'EST'):
            field_name = tokens[0][1]  # NOMEN
            object_name = tokens[1][1]  # SERVUS
            
            if object_name not in self.variables:
                self.error(f"'{object_name}' non declaratur", f"Object '{object_name}' not declared")
            
            # Ensure the object is a dictionary (struct)
            if not isinstance(self.variables[object_name], dict):
                # Initialize as dict if it's not already
                self.variables[object_name] = {}
            
            # Field assignment: FIELDGENITIVE EST STRING
            if len(tokens) == 4 and tokens[3][0] == 'STRING':
                self.variables[object_name][field_name] = tokens[3][1]
                return None
            
            # Field assignment: FIELDGENITIVE EST NUMBER
            if len(tokens) == 4 and tokens[3][0] == 'NUMBER':
                self.variables[object_name][field_name] = tokens[3][1]
                return None
            
            # Field assignment: FIELDGENITIVE EST VARIABLE
            if len(tokens) == 4 and tokens[3][0] == 'VARIABLE':
                source_var = tokens[3][1]
                if source_var not in self.variables:
                    self.error(f"'{source_var}' non declaratur", f"Variable '{source_var}' not declared")
                self.variables[object_name][field_name] = self.variables[source_var]
                return None
            
            # Field assignment: FIELDGENITIVE EST FIELD2GENITIVE2 (copy from another field)
            if len(tokens) == 5 and tokens[3][0] == 'VARIABLE' and tokens[4][0] == 'GENITIVE':
                source_field = tokens[3][1]
                source_object = tokens[4][1]
                if source_object not in self.variables:
                    self.error(f"'{source_object}' non declaratur", f"Object '{source_object}' not declared")
                if not isinstance(self.variables[source_object], dict):
                    self.error(f"'{source_object}' non est structura", f"'{source_object}' is not a struct")
                if source_field not in self.variables[source_object]:
                    self.error(f"Campus '{source_field}' in '{source_object}' non existit", 
                              f"Field '{source_field}' in '{source_object}' does not exist")
                self.variables[object_name][field_name] = self.variables[source_object][source_field]
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
            
            # VARIABLE EST VOCA ... (function call)
            if len(tokens) >= 4 and tokens[2] == ('KEYWORD', 'VOCA'):
                # Mark that we're expecting a return value
                self.variables['__CALLING_VAR__'] = var_name
                # Call function and jump to it
                jump_addr = self.call_function(tokens[3:])
                return jump_addr
            
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
                # Throw an ERROR exception that can be caught with CAPEERROR
                if not self.exception_handlers:
                    # No handler, use normal error
                    self.error("Divisio per nihil", "Division by zero")
                else:
                    # Handler exists, throw catchable exception
                    # Find ERROR handler
                    for handler_type, handler_line in reversed(self.exception_handlers):
                        if handler_type == 'ERROR':
                            self.current_exception = {'type': 'ERROR', 'message': 'Divisio per nihil'}
                            self.exception_throw_line = self.line_index + 1
                            # Signal that we need to jump to handler
                            raise LatinExceptionThrown(handler_line)
                    # No ERROR handler found
                    self.error("Divisio per nihil", "Division by zero")
            return values[0] // values[1]
        
        return 0
    
    def call_function(self, tokens: List[Tuple[str, str]]):
        """Call a function with given arguments."""
        if len(tokens) < 1:
            self.error("VOCA requirit nomen functionis", "VOCA requires function name")
        
        # First token should be the function name (in accusative case)
        if tokens[0][0] != 'VARIABLE':
            self.error("VOCA requirit nomen functionis", "VOCA requires function name")
        
        func_name = tokens[0][1]
        
        # Check if function exists
        if func_name not in self.functions:
            self.error(f"Functio '{func_name}' non definitur", f"Function '{func_name}' not defined")
        
        func_def = self.functions[func_name]
        params = func_def['params']
        
        # Get arguments
        args = []
        for i in range(1, len(tokens)):
            token_type, token_value = tokens[i]
            if token_type == 'NUMBER':
                args.append(token_value)
            elif token_type == 'STRING':
                args.append(token_value)
            elif token_type == 'VARIABLE':
                if token_value not in self.variables:
                    self.error(f"'{token_value}' non declaratur", f"Variable '{token_value}' not declared")
                args.append(self.variables[token_value])
            else:
                self.error("Argumenta invalida", "Invalid arguments")
        
        # Check argument count
        if len(args) != len(params):
            self.error(f"Functio '{func_name}' requirit {len(params)} argumenta", 
                      f"Function '{func_name}' requires {len(params)} arguments")
        
        # Save current variable state
        saved_vars = self.variables.copy()
        
        # Bind parameters to arguments
        for param, arg in zip(params, args):
            self.variables[param] = arg
        
        # Save return address and variables on call stack
        self.call_stack.append({
            'return_line': self.line_index,
            'saved_vars': saved_vars
        })
        
        # Jump to function start
        return func_def['start_line']


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
