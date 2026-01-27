# The LATIN Programming Language

LATIN is a programming language designed for educational purposes, focusing on simplicity and ease of understanding. It draws inspiration from natural languages, particularly Latin, to create a syntax that is both intuitive and expressive.

LATIN is an acronym for `Latin Ain't This Insufferable Normally`. We normally distinguish between LATIN the programming language and Latin the natural language by writing the former in all caps.

## Key Features

- **Natural Language Syntax**: LATIN uses a syntax that resembles ancient Latin language, making it easier for Latin speaking beginners to start coding.
- **Syntax Simplicity**: The language is designed to minimize complexity with formatting, strange characters and other distractions, making it accessible for beginners. The programming language only uses upper case Roman letters. **LATIN programs contain no spaces** - word boundaries are determined by Latin morphology. Digits are not used in LATIN programs. Numbers are represented using words.
- **Educational Focus**: LATIN is intended to be a stepping stone for learners to understand programming concepts before moving on to more complex languages.
- **Cross-Platform**: LATIN can be run on various platforms, making it versatile for different development environments.

## Getting Started

### Variables

In LATIN, variables are declared using the `SIT` keyword (from Latin "sit" meaning "let it be") followed by the variable name. Variable names must consist of uppercase letters only and follow the normal Latin grammar rules for nouns. Variables can hold either integers (represented as Roman numerals) or strings (text in quotes).

**Latin Noun Rules:**
Variable names in LATIN must be valid Latin nouns, which means they must:

- Belong to one of the five declensions (first through fifth)
- Have a proper nominative singular form
- Be either masculine, feminine, or neuter gender
- Follow traditional Latin spelling conventions (no J, U, or W - use I, V instead)

Common examples by declension:

- First declension (mostly feminine): PUELLA (girl), ROSA (rose), AQUA (water)
- Second declension (mostly masculine/neuter): AMICUS (friend), SERVUS (slave), BELLUM (war)
- Third declension (all genders): REX (king), CIVIS (citizen), CORPUS (body)
- Fourth declension: MANUS (hand), GRADUS (step)
- Fifth declension: RES (thing), DIES (day)

**Latin Cases:**
LATIN uses the traditional Latin case system to determine the grammatical role of variables in statements:

- **Nominative** - The subject case, used for:
  - The variable being declared after SIT
  - The left side of assignments (before EST)
  - The subject of comparisons (before AEQUAT)
  - Example: NUMERUS, PRIMUS, AMICUS

- **Accusative** - The direct object case, used for:
  - The object being printed with SCRIBE
  - The thing being added (first argument to ADDE)
  - The thing being subtracted (first argument to DEME)
  - The right side of comparisons (after AEQUAT)
  - Example: NUMERUM, PRIMUM, AMICUM (typically -UM ending)

- **Dative** - The indirect object case ("to" or "for"), used for:
  - The recipient in addition (second argument to ADDE)
  - Meaning "add X to Y" where Y is in dative
  - Example: NUMERO, PRIMO, AMICO (typically -O ending in 2nd declension)

- **Ablative** - The separation case ("from" or "by means of"), used for:
  - The source in subtraction (second argument to DEME)
  - Meaning "subtract [accusative] from [ablative]"
  - The case determines the role: DEME NUMERUM (acc) PRIMO (abl) = "subtract NUMERUM from PRIMO"
  - If you swap the cases, you swap the roles: DEME PRIMUM (acc) NUMERO (abl) = "subtract PRIMUM from NUMERO"
  - Example: NUMERO, PRIMO, AMICO (same as dative in 2nd declension)

- **Genitive** - The possessive case ("of")
  - Reserved for future use in LATIN
  - Example: NUMERI, PRIMI, AMICI

- **Vocative** - The address case (calling someone)
  - Reserved for future use in LATIN
  - Example: NUMERE, PRIME, AMICE

When using variables in different contexts, they must be declined to the appropriate case (nominative, genitive, dative, accusative, ablative, or vocative) according to their grammatical function in the statement.

Example:

~~~latin
SITAMICUS
SITPUELLA
SITBELLVM
~~~

### Parsing and Word Boundaries

LATIN programs contain **no whitespace**. The parser determines word boundaries using Latin morphological rules:

- **Keywords** (SIT, EST, etc.) are recognized by exact pattern matching
- **Variable names** are identified by valid Latin noun forms with their declension endings
- **Case endings** (-us, -a, -um, -ae, -is, -em, -i, -o, -es, etc.) signal word boundaries
- **Verb conjugations** follow standard Latin patterns

**Parsing Strategy:**
The parser uses a greedy left-to-right algorithm that attempts to match the longest valid Latin word at each position. When multiple valid parsings exist, the parser:

1. Prefers keywords over variable names
2. Prefers previously declared variables
3. Otherwise, the program is considered ambiguous

**Ambiguous Programs:**
Some LATIN programs may have multiple valid interpretations. This is considered a **feature, not a bug**. Ambiguous programs encourage programmers to:

- Choose clearer variable names
- Use proper Latin vocabulary
- Appreciate the inherent complexity of natural language parsing

Example of potential ambiguity:

~~~latin
SITAMO
~~~

Could be parsed as: `SIT AMO` (let there be "I love") or `SITAMO` (a hypothetical single word).

To avoid ambiguity, use well-formed Latin nouns from standard declensions.

### Numbers

In LATIN, numbers are represented using roman numerals for numbers:

- I: 1
- V: 5
- X: 10
- L: 50
- C: 100
- D: 500
- M: 1000
- Combinations of these letters can be used to represent other numbers (e.g., IV for 4, IX for 9, XL for 40, etc.).
Examples:

~~~latin
MXXIV  ; represents 1024
DCCCXC  ; represents 890
~~~

### Comments

Comments in LATIN begin with a semicolon (`;`) and extend to the end of the line. Comments are ignored by the parser and can be used to explain code or add notes.

Example:

~~~latin
SITNUMERUS           ; declare a variable
NUMERUSESTXLII       ; set it to 42
SCRIBENUMERUM        ; output the value
~~~

Comments allow programmers to document their Latin grammar choices and explain the meaning of variable names without affecting program execution.

### Control Structures

LATIN includes basic control structures such as conditionals and loops, using Latin keywords.

#### If Statement

- **SI** (if) - conditional statement
- **ALITER** (else) - else clause for conditionals (from Latin "aliter" meaning "otherwise")
- **AEQUAT** (equals) - equality comparison
- **MAIVS** (greater) - greater than comparison (from "maior")
- **MINOR** (less) - less than comparison
- **FINIS** (end) - marks the end of a control structure block

Syntax:

~~~latin
SI[nominative][comparison][value]
[statements]
FINIS
~~~

Or with else:

~~~latin
SI[nominative][comparison][value]
[statements if true]
ALITER
[statements if false]
FINIS
~~~

Examples:

~~~latin
SITNUMERUS
NUMERUSESTX
SINUMERUSAEQUATX     ; if NUMERUS equals 10
SCRIBENUMERUM        ; then print it
FINIS                ; end if

SINUMERUSMAIVSV      ; if NUMERUS > 5
SCRIBENUMERUM
FINIS

SINUMERUSMINORXX     ; if NUMERUS < 20
SCRIBENUMERUM
FINIS
~~~

Example with else:

~~~latin
SITNUMERUS
SITSUMMA
NUMERUSESTX
SINUMERUSAEQUATX     ; if NUMERUS == 10
SUMMAESTC            ; then SUMMA = 100
ALITER               ; else
SUMMAESTL            ; SUMMA = 50
FINIS                ; end if
SCRIBESUMMA          ; prints C (or L if condition was false)
~~~

#### While Loop

- **DUM** (while) - loop keyword

Syntax:

~~~latin
DUM[nominative][comparison][value]
[statements]
FINIS
~~~

Example - countdown from 10:

~~~latin
SITNUMERUS
NUMERUSESTX          ; start at 10
DUMNUMERUSMAIVSI     ; while NUMERUS > 1
SCRIBENUMERUM        ; print current value
NUMERUSESTDEMENUMEROI ; subtract 1
FINIS                ; end loop
~~~

### Arithmetic Operations

LATIN supports four basic arithmetic operations, all using proper Latin grammar:

- **ADDE** [accusative] [dative] - Addition ("add X to Y")
- **DEME** [accusative] [ablative] - Subtraction ("subtract X from Y")
- **MVLTIPLICA** [accusative] [accusative] - Multiplication ("multiply")
- **DVCE** [accusative] [ablative] - Integer division ("divide")

### String Operations

LATIN provides comprehensive string manipulation capabilities:

- **IVNGE** [accusative] [accusative] - String concatenation ("join")
- **INCIPITCVM** [nominative] [ablative] - Check if string starts with substring ("begins with")
- **FINITVRCVM** [nominative] [ablative] - Check if string ends with substring ("finishes with")
- **CONTINET** [nominative] [accusative] - Check if string contains substring ("holds/contains")
- **INDICEDE** [nominative] [ablative] - Find index position of substring ("point out from")
- **AEQUAT** - String equality comparison (also works with numbers)

All string operations accept either string literals (in double quotes) or variables. When using variables, follow proper Latin case grammar:

- INCIPITCVM/FINITVRCVM/INDICEDE use ablative for the second argument (CVM "with" and DE "from" take ablative)
- CONTINET uses accusative for the second argument (direct object)

String operations that check conditions (INCIPITCVM, FINITVRCVM, CONTINET) return **I** (Roman numeral 1) for true and **NIHIL** (0) for false. INDICEDE returns the position as a Roman numeral, or NIHIL if not found.

Examples:

~~~latin
; String concatenation
SITNOMEN
SITSALVTATIO
NOMENEST"MARCVS"
SALVTATIOESTIVNGE"SALVE"NOMEN
SCRIBESALVTATIONE    ; outputs: SALVEMARCVS

; String checking
SITNOMEN
SITPRAEFIXVM
SITRESULTAT
NOMENEST"CAESAR"
PRAEFIXVMEST"CAE"

; Check if starts with "CAE" (using string literal)
RESULTATESTINCIPITCVMNOMEN"CAE"
SCRIBERESULTAT       ; outputs: I (true)

; Check if starts with prefix variable (using ablative case)
RESULTATESTINCIPITCVMNOMENPRAEFIXO
SCRIBERESULTAT       ; outputs: I (true)

; Check if ends with "SAR"
RESULTATESTFINITVRCVMNOMEN"SAR"
SCRIBERESULTAT       ; outputs: I (true)

; Check if contains "AES"
RESULTATESTCONTINETNOMEN"AES"
SCRIBERESULTAT       ; outputs: I (true)

; Find position of "SAR"
RESULTATESTINDICEDENOM EN"SAR"
SCRIBERESULTAT       ; outputs: III (position 3)

; String equality
SINOMENAEQUAT"CAESAR"
SCRIBE"Name is CAESAR"
FINIS
~~~

### Arithmetic Examples

~~~latin
SITPRIMUS
SITSECUNDUS
SITTERTIUS

; Addition: 20 + 22 = 42
PRIMUSESTXX
SECUNDUSESTXXII
TERTIUSESTADDEPRIMUMSECUNDO
SCRIBETERTIUM        ; outputs: XLII

; Multiplication: 6 * 7 = 42
PRIMUSESTVI
SECUNDUSESTVII
TERTIUSESTMVLTIPLICAPRIMUMSECUNDUM
SCRIBETERTIUM        ; outputs: XLII

; Division: 100 / 2 = 50
PRIMUSESTC
SECUNDUSESTII
TERTIUSESTDVCEPRIMOSECUNDO
SCRIBETERTIUM        ; outputs: L
~~~

### Functions

LATIN supports function definitions and calls using Latin terminology.

*Note: Function support is planned for future releases.*

- **FAC** (do/make) - function definition
- **REDDO** (return) - return statement

### User Input

LATIN supports reading user input with the **LEGO** keyword (Latin for "I read" or "I gather"):

~~~latin
SITNOMEN
SITNUMERUS

SCRIBE"What is your name?"
LEGONOMEN            ; reads text input

SCRIBE"Enter a number:"
LEGONUMERUS          ; reads Roman numeral
~~~

LEGO automatically detects whether the input is a Roman numeral or text:
- If the input is a valid Roman numeral (I, V, X, L, C, D, M), it's stored as an integer
- Otherwise, it's stored as a string
- Strings can optionally be entered with quotes, which will be removed

### Interactive REPL

LATIN includes an interactive Read-Eval-Print Loop for experimenting with the language:

~~~bash
# Start the REPL
python3 latin.py --repl

# Or just run without arguments
python3 latin.py
~~~

REPL commands:

- Type LATIN code directly and press Enter
- **VALE** - quit the REPL (Latin for "farewell")
- **ANGLICE** - switch to English error messages
- **LATINE** - switch to Latin error messages

Example REPL session:

~~~latin
LATIN> SITNUMERUS
LATIN> NUMERUSESTXLII
LATIN> SCRIBENUMERUM
XLII
LATIN> VALE
Vale! (Goodbye!)
~~~

### Running LATIN Programs

~~~bash
# Run a LATIN program
python3 latin.py program.lat

# Run with English error messages (default is Latin)
python3 latin.py program.lat --english

# Start interactive REPL
python3 latin.py --repl
~~~

### Output Format

All numeric values are output as Roman numerals:

- Zero is represented as **NIHIL** ("nothing" in Latin)
- Positive integers use standard Roman numeral notation
- Examples: XLII (42), C (100), MCMXC (1990)

### Standard Library

*Note: Standard library functions are planned for future releases. Currently, LATIN supports built-in operations only.*

Planned features:

- `LEGO` (read) - input from user
- Additional string manipulation functions

## Getting Help

### Error Messages

LATIN provides error messages in both Latin (default) and English:

**Latin Error Messages (Default):**

- `ERRATUM: '[word]' non intellegitur` - word not understood
- `ERRATUM: '[var]' non declaratur` - variable not declared
- `ERRATUM: Syntax incorrecta` - incorrect syntax
- `ERRATUM: Divisio per nihil` - division by zero

**English Error Messages** (use `--english` flag or type `ANGLICE` in REPL):

- `Unknown word`
- `Variable not declared`
- `Invalid syntax`  
- `Division by zero`

## Community and Resources

Join the LATIN programming community to share your projects, ask questions, and learn from others. Visit our [GitHub repository] ([https://github.com/anders-wartoft/latin](https://github.com/anders-wartoft/latin))
