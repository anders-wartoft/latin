# LATIN Programming Language - Quick Reference

## Running Programs

```bash
# Run a LATIN program
python3 latin.py program.lat

# Run with English error messages
python3 latin.py program.lat --english

# Start interactive REPL
python3 latin.py --repl
```

## Keywords

- **SIT** - Declare variable ("let it be")
- **EST** - Assignment ("is")
- **SI** - If conditional
- **ALITER** - Else clause ("otherwise")
- **DUM** - While loop ("while")
- **FINIS** - End block
- **SCRIBE** - Print output ("write")
- **LEGO** - Read user input ("I read/gather")

## Operations

### Arithmetic

- **ADDE** - Addition (add [acc] to [dat])
- **DEME** - Subtraction (subtract [acc] from [abl])
- **MVLTIPLICA** - Multiplication
- **DVCE** - Integer division ("divide")

### String Operations

- **IVNGE** - String concatenation ("join") [acc] [acc]
- **INCIPITCVM** - Starts with ("begins with") [nom] [abl]
- **FINITVRCVM** - Ends with ("finishes with") [nom] [abl]
- **CONTINET** - Contains ("holds/contains") [nom] [acc]
- **INDICEDE** - Index of ("point out from") [nom] [abl]

Note: All string operations accept string literals or variables

### Comparison

- **AEQUAT** - Equals (=) - works with numbers and strings
- **MAIVS** - Greater than (>)
- **MINOR** - Less than (<)

## Data Types

- **Integers** - Represented as Roman numerals (I, V, X, L, C, D, M)
- **Strings** - Text in double quotes: "text here"
- **NIHIL** - Zero ("nothing")

## Latin Cases

- **Nominative** (-US, -A, -UM): Subject, before EST
- **Accusative** (-UM, -AM): Direct object, after SCRIBE, first arg to operations
- **Dative** (-O, -AE): "to/for", second arg to ADDE
- **Ablative** (-O, -A): "from", second arg to DEME

## Common Variables

```latin
NUMERUS/NUMERUM/NUMERO  - number
PRIMUS/PRIMUM/PRIMO     - first
SECUNDUS/SECUNDUM/SECUNDO - second
TERTIUS/TERTIUM/TERTIO  - third
QUARTUS/QUARTUM/QUARTO  - fourth
QUINTUS/QUINTUM/QUINTO  - fifth
NOMEN/NOMEN/NOMINI/NOMINE - name
PRAEFIXVM/PRAEFIXVM/PRAEFIXO - prefix
RESULTAT/RESULTATUM/RESULTATO - result
INDEX/INDICEM/INDICI/INDICE - index
```

## Examples

### Hello World

```latin
SITNUMERUS
NUMERUSESTXLII
SCRIBENUMERUM
```

### Addition

```latin
SITPRIMUS
SITSECUNDUS
SITTERTIUS
PRIMUSESTXX
SECUNDUSESTXXII
TERTIUSESTADDEPRIMUMSECUNDO  ; add PRIMUM to SECONDO
SCRIBETERTIUM
```

### Conditional

```latin
SITNUMERUS
NUMERUSESTX
SINUMERUSAEQUATX
SCRIBENUMERUM
FINIS
```

### Loop (countdown from 10)

```latin
SITNUMERUS
NUMERUSESTX
DUMNUMERUSMAIVSI
SCRIBENUMERUM
NUMERUSESTDEMENUMERVI
FINIS
```

### User Input

```latin
SITNOMEN
SITNUMERUS
SCRIBE"Quid est nomen tuum?"
LEGONOMEN
SCRIBE"Quantus numerus?"
LEGONUMERUS
```

### Multiplication

```latin
SITPRIMUS
SITSECUNDUS
PRIMUSESTVI
SECUNDUSESTVII
TERTIUSESTMVLTIPLICAPRIMUMSECUNDUM
SCRIBETERTIUM
```

### String Operations Example

```latin
SITNOMEN
SITPRAEFIXVM
SITRESULTAT
NOMENEST"CAESAR"
PRAEFIXVMEST"CAE"

; Check if starts with "CAE" (literal)
RESULTATESTINCIPITCVMNOMEN"CAE"  ; returns I (true)

; Check if starts with prefix (variable in ablative)
RESULTATESTINCIPITCVMNOMENPRAEFIXO  ; returns I (true)

; Check if ends with "SAR"
RESULTATESTFINITVRCVMNOMEN"SAR"  ; returns I (true)

; Check if contains "AES"
RESULTATESTCONTINETNOMEN"AES"    ; returns I (true)

; Find index of "SAR"
RESULTATESTINDICEDENOMEN"SAR"    ; returns III (position 3)

; String equality
SINOMENAEQUAT"CAESAR"
SCRIBE"Match found"
FINIS
```

## REPL Commands

- **VALE** - Quit REPL ("farewell")
- **ANGLICE** - Switch to English errors
- **LATINE** - Switch to Latin errors

## Error Messages

### Latin (Default)

- `ERRATUM: '[word]' non intellegitur` - word not understood
- `ERRATUM: '[var]' non declaratur` - variable not declared
- `ERRATUM: Syntax incorrecta` - incorrect syntax
- `ERRATUM: Divisio per nihil` - division by zero

### English (use --english flag)

- `Unknown word`
- `Variable not declared`
- `Invalid syntax`
- `Division by zero`

## Roman Numerals

Numbers are input and output as Roman numerals:

- I=1, V=5, X=10, L=50, C=100, D=500, M=1000
- Subtractive notation: IV=4, IX=9, XL=40, XC=90, CD=400, CM=900
- NIHIL = 0 (nothing)

## Notes

- Programs have NO SPACES between words
- Comments start with `;`
- All letters must be uppercase
- Use classical spelling: V for U, I for J
- BELLVM not BELLUM, MANVS not MANUS
