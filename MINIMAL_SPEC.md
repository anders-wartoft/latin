# LATIN Minimal Language Specification

Version: 0.2 (Feature-Complete Edition)

## Overview

This document defines the absolute minimum feature set for a working LATIN interpreter. The goal is to have the smallest possible language that can still perform basic computation while maintaining the prank spirit of requiring Latin grammar knowledge.

## Character Set

- **Only uppercase Roman letters**: A-Z (excluding J, U, W as per classical Latin)
- **No whitespace**: Programs are continuous strings
- **Newlines**: Used only to separate statements

## Numbers

**Roman Numerals Only:**

- I = 1
- V = 5  
- X = 10
- L = 50
- C = 100
- D = 500
- M = 1000

Standard Roman numeral rules apply:

- Additive: VI = 6, XV = 15
- Subtractive: IV = 4, IX = 9, XL = 40, XC = 90, CD = 400, CM = 900

## Comments

Comments begin with a semicolon (`;`) and extend to the end of the line.

- Comments are completely ignored by the parser
- They do not affect tokenization or execution
- Useful for explaining Latin grammar choices and variable meanings

Example:

```latin
SITNUMERUS     ; declare NUMERUS (number)
NUMERUSESTX    ; assign 10 to NUMERUS
```

## Keywords (Extended Set)

Core keywords:

1. **SIT** - Variable declaration ("let it be")
2. **EST** - Assignment/comparison ("is")
3. **SI** - Conditional ("if")
4. **FINIS** - End block ("end")
5. **SCRIBE** - Output ("write")

Additional keywords:
6. **DUM** - While loop ("while")
7. **ALITER** - Else clause ("otherwise")
8. **FAC** - Function declaration ("do/make")
9. **REDDO** - Return value ("give back")
10. **AVDI** - Log to stderr ("listen/hear")
11. **NOTA** - Debug log to stderr ("note/mark")
12. **LEGE** - Read input ("read")
13. **IACE** - Throw exception ("throw")
14. **CAPE** - Catch exception ("catch")

## Operations (Extended Set)

Arithmetic operations:

1. **ADDE** - Addition ("add")
   - Usage: `ADDE[accusative][dative]` - "add [accusative] to [dative]"
2. **DEME** - Subtraction ("subtract")
   - Usage: `DEME[accusative][ablative]` - "subtract [accusative] from [ablative]"
3. **DUC** - Multiplication ("lead/multiply")
   - Usage: `DUC[accusative][ablative]` - "multiply [accusative] by [ablative]"
4. **DIVIDE** - Division ("divide")
   - Usage: `DIVIDE[accusative][ablative]` - "divide [accusative] by [ablative]"

Comparison operations:
5. **AEQUAT** - Equals comparison ("equals")
6. **MAIOR** - Greater than ("greater")
7. **MINOR** - Less than ("lesser")

String operations (on string variables):
8. **INCIPIT** - Starts with ("begins")
9. **DESINIT** - Ends with ("ends")
10. **CONTINET** - Contains ("contains")
11. **INDEX** - Find position ("index")

Note: String operations use the genitive case for the search pattern

## Grammar Rules

### Variable Names

- Must be valid Latin nouns
- Must be from the five Latin declensions
- Must decline properly by case:
  - **Nominative**: subject, left side of assignment
  - **Accusative**: direct object, the thing being acted upon
  - **Dative**: indirect object, "to" or "for" (used with ADDE)
  - **Ablative**: "from" or "by means of" (used with DEME, DUC, DIVIDE)
  - **Genitive**: possession, "of" (used for struct field access)
  - **Vocative**: direct address (used in exception handling with CAPE)

### Common Variable Examples

For simplicity, stick to second declension masculine (-US, -UM, -O endings):

- NUMERUS (number) - nominative singular
- NUMERUM - accusative singular
- NUMERO - dative/ablative singular (same form in 2nd declension!)

## Syntax

### Variable Declaration

```latin
SIT[nominative-noun]
```

Example:

```latin
SITNUMERUS
```

### Assignment

```latin
[nominative]EST[value]
```

Example:

```latin
NUMERUSESTX
```

Assigns value X (10) to NUMERUS.

### Arithmetic Assignment

```latin
[nominative]ESTADDE[accusative][dative]
[nominative]ESTDEME[accusative][ablative]
```

Examples:

```latin
NUMERUSESTADDEXV        ; add X (acc) to V (dat) = 15
NUMERUSESTDEMEXLNUMERO  ; subtract XL (acc) from NUMERO (abl)
```

### Output

```latin
SCRIBE[accusative]
```

Example:

```latin
SCRIBENUMERUM
```

### Conditionals

```latin
SI[nominative]AEQUAT[accusative]
[statements]
FINIS
```

Example:

```latin
SINUMERUSAEQUATX
SCRIBENUMERUM
FINIS
```

## Complete Example Programs

### Hello World (Number Edition)

```latin
SITNUMERUS
NUMERUSESTXLII
SCRIBENUMERUM
```

Output: `42`

### Addition

```latin
SITNUMERUS
NUMERUSESTADDEXXX
SCRIBENUMERUM
```

Output: `60`

### Conditional

```latin
SITNUMERUS
NUMERUSESTX
SINUMERUSAEQUATX
SCRIBENUMERUM
FINIS
```

Output: `10`

### Complex Example

```latin
SITPRIMUS
SITSECUNDUS
SITTERTIUS
PRIMUSESTXX
SECUNDUSESTXXII
TERTIUSESTADDEPRIMUMSECUNDO   ; add PRIMUM (acc) to SECONDO (dat)
SCRIBETERTIUM
```

Output: `42`

## Parser Implementation Notes

### Parsing Strategy

1. **Newline-separated statements**: Each statement is on its own line
2. **Keyword matching**: Greedily match known keywords (SIT, EST, SI, FINIS, SCRIBE, ADDE, DEME, AEQUAT)
3. **Roman numeral matching**: Match valid Roman numeral patterns
4. **Variable matching**: Match declared variable names with proper case endings
5. **Remaining text**: Should resolve to a valid Latin noun form

### Declension Lookup

The parser needs a dictionary of valid Latin nouns with their declined forms:

- NUMERUS (nominative) → NUMERUM (accusative), NUMERO (dative/ablative)
- PRIMUS (nominative) → PRIMUM (accusative), PRIMO (dative/ablative)
- SECUNDUS (nominative) → SECUNDUM (accusative), SECUNDO (dative/ablative)
- TERTIUS (nominative) → TERTIUM (accusative), TERTIO (dative/ablative)

Note: In 2nd declension masculine, dative and ablative singular have the same form (-o).

### Tokenization Example

Input: `NUMERUSESTX`

1. Try to match keyword from start: No match
2. Try to match variable: Check if NUMERUS is declared → Yes
3. Consume NUMERUS
4. Try to match keyword: EST → Match
5. Consume EST
6. Try to match Roman numeral: X → Match
7. Consume X
8. End of statement

Result: `[VAR:NUMERUS, KW:EST, NUM:10]`

## Implementation Requirements

### Minimum Data Structures

1. **Symbol table**: Maps variable names (nominative form) to integer values
2. **Declension table**: Maps nominative forms to accusative/ablative forms
3. **Token stream**: List of parsed tokens
4. **Program counter**: For executing statements

### Minimum Functions

1. `tokenize(line)` → list of tokens
2. `parse_statement(tokens)` → AST node
3. `execute_statement(ast_node)` → side effects
4. `main_loop()` → read lines, parse, execute

## Error Handling

For the minimal implementation, errors should be simple:

- **Unknown word**: "ERRATUM: '[word]' non intellegitur" (word not understood)
- **Undeclared variable**: "ERRATUM: '[var]' non declaratur" (variable not declared)
- **Invalid syntax**: "ERRATUM: Syntax incorrecta" (incorrect syntax)
- **Case mismatch**: "ERRATUM: Casus grammaticus incorrectus" (wrong grammatical case)

## Features Now Implemented

The language has grown beyond the minimal spec and now includes:

- ✅ While loops (DUM)
- ✅ Functions with parameters and return values (FAC/REDDO)
- ✅ String literals and text output (using quotes)
- ✅ User input (LEGE)
- ✅ Multiplication and division (DUC/DIVIDE)
- ✅ String comparison operations
- ✅ ELSE clauses (ALITER)
- ✅ Comments (semicolons)
- ✅ Logging to stderr (AVDI/NOTA)
- ✅ Exception handling (IACE/CAPE with vocative case)
- ✅ Struct/object field access using genitive case
- ✅ String operations (starts with, ends with, contains, index)
- ✅ Automatic declension generation for new variables

For complete feature documentation, see README.md and FEATURES.md

## Next Steps

1. Write a lexer/tokenizer
2. Build declension dictionary for common nouns
3. Implement parser with AST generation
4. Create interpreter that executes AST
5. Add REPL (if feeling ambitious)
