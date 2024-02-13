# Python Essentials 1 - Module 2: Python Data Types, Variables, Operators and Basic I/O Operations

## Section 1: The "Hello World! program

## Section 2: Python literals

### Underscores in integers and floats

Python (apparently since Python 3.6) supports using underscores (_) as a substitute for commas for breaking up large integer and float variables such as 100,000 being represented as `100_000`. With strings, obviously, the underscore is part of the string.

`print(100_000)`

`100000`

`print("100_000")`

`100_000`

### Binary, Octal and Hexadecimal

Binary, octal and hexadecimal numbers can be represented as **literals** using this notation. An easy way to remember hexadecimal is that many memory addresses start with `0x` or the simple mnemonic of *box*:

| Syntax:      | Numeric base:         | Example: |
| -------------| --------------------- | -------- |
| `0b` or `0B` | Binary (base-2)       | `0b1010` |
| `0o` or `0O` | Octal (base-8)        | `0o70`   |
| `0x` or `0X` | Hexademical (base-16) | `0x2AF`  |

**Note:** This numerical base notation is case-insensitive.

While not specifically mentioned in the Python Essentials 1 notes, it's worth knowing that *by default Python 3 outputs to standard Decimal (base-10) when performing calculations in different numerical bases.* However, there are the `bin()`, `oct()` and `hex()` functions which maintain the chosen notation:

`>>> print(0b1 + 0b1)`

`2`

`>>> print(bin(0b1 + 0b1))`

`0b10`

Binary values can be easily calculated by just counting the ones in each column like so, for example, the number `48` in decimal (base-10) is represented as:

| 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| -- | -- | -- | - | - | - | - |
| `0`| `1`| `1`|`0`|`0`|`0`|`0`| 

## Section 3: Operators – data manipulation tools

### Order of operations

Python uses an order of operations similar to PEMDAS, the US counterpart to BODMAS:

1. **P**arentheses or brackets – `()`
2. **E**xponentiation or of – `**` or x^y or x<sup>y</sup>
3. **M**ultiplication – `*` or ×
4. **D**ivision – `/` or ÷
5. **A**ddition – `+`
6. **S**ubtraction – `-`

### Division `/` and floor division `//`

Python has two forms of division built-in:

1. **Division** (`/`) is the standard division operator which will *always* output a float value. For example, `9 / 3` will output `3.0`
2. **Floor division** (`//`) creates an integer removing all the values beyond the decimal point. For example, running floor division on these outputs `3` each time: `3.1`, `3.5`, `3.9`

If it's easier, you could refer to them as *float division* and *integer division* respectively. Ceiling division is the opposite of floor division, but there's no built-in operator for it and is outside the scope of the PCEP.

### Variables

Like many interpreted programming languages, Python uses **dynamic variables** which means a variable's datatype is defined by the value itself rather than specific datatype keyword designation. 

Python variables are *case-sensitive* which means that `y = 1` and `Y = 2` can technically co-exist in the same block of code together while meaning different things.

### Variable datatypes

For the PCEP, these datatypes are the only ones covered though there are many more built into Python 3:

* Integer – whole numbers such as `1`, `10` and `100`
* Float – decimal numbers such as `1.0`, `.5` and `1.23`
* String – a character or series of characters using single (`'`) or double (`"`) quotes such as `"Hello"`, `10` and `"This is a sentence."`
* Boolean – either `True` or `False` (booleans are case-sensitive)
