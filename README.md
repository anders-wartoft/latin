# LATIN programming language


LATIN is a programming language designed for educational purposes, focusing on simplicity and ease of understanding. It draws inspiration from natural languages, particularly Latin, to create a syntax that is both intuitive and expressive.

LATIN is an acronym for `Latin Ain't This Insufferable Normally`. We normally distinguish between LATIN the programming language and Latin the natural language by writing the former in all caps.

## Key Features

- **Natural Language Syntax**: LATIN uses a syntax that resembles ancient Latin language, making it easier for Latin speaking beginners to start coding.
- **Syntax Simplicity**: The language is designed to minimize complexity with formatting, strange characters and other distractions, making it accessible for beginners. The programming language only uses upper case Roman letters. **LATIN programs contain no spaces** - word boundaries are determined by Latin morphology. Digits are not used in LATIN programs. Numbers are represented using words.
- **Educational Focus**: LATIN is intended to be a stepping stone for learners to understand programming concepts before moving on to more complex languages.
- **Cross-Platform**: LATIN can be run on various platforms, making it versatile for different development environments.

## Getting Started

### Variables

In LATIN, variables are declared using the `SIT` keyword (from Latin "sit" meaning "let it be") followed by the variable name. Variable names must consist of uppercase letters only and follow the normal Latin grammar rules for nouns.

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

- **If Statement**: `SI` (if), `ALIOQUANDO` (else)
- **While Loop**: `DUM` (while)
Example:

~~~latin
SIAMICUSESTPUELLAALIOQUANDO
    ; code if AMICUS is PUELLA
DUMAMICUSESTPUELLA
    ; code while AMICUS is PUELLA
~~~

### Functions

LATIN supports function definitions and calls using Latin terminology.

- **Function Definition**: `FAC` (do/make)
- **Return Statement**: `REDDO` (return)

Example:

~~~latin
FACAMICUM

    ; function body
    REDDOAMICUM
~~~

### Standard Library

LATIN comes with a standard library of functions for common tasks, all named using Latin words.

- `PRINTA` (print)
- `LEGO` (read)
- `SUMMA` (sum)
- `MULTIPLICATIO` (multiply)

Example:

~~~latin
PRINTAAMICUS
LEGOAMICUS
SUMMAUNUSDUO
~~~

Note that you use different forms of the words based on Latin grammar rules.
So if you want to add a number to a variable, you would use the accusative case for the number and the nominative case for the variable.

Example:

~~~latin
SITAMICUS
AMICUSESTSUMMAUNUSDUO  ; AMICUS is 3
PRINTAAMICUS           ; prints 3
~~~

Here we can see one of the beauties of LATIN - the grammar rules help clarify the roles of each word in the statement. We can even scramble the words around a bit and still have a valid statement:

~~~latin
SUMMAUNUSDUOAMICUSEST  ; AMICUS is 3
PRINTAAMICUS           ; prints 3
~~~

## Community and Resources

Join the LATIN programming community to share your projects, ask questions, and learn from others. Visit our [GitHub repository] ([https://github.com/anders-wartoft/latin](https://github.com/anders-wartoft/latin))
