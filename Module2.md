# Python Essentials 1 - Module 2: Python Data Types, Variables, Operators and Basic I/O Operations

## Binary, Octal and Hexadecimal
Binary, octal and hexadecimal numbers can be represented as **literals** using this notation. An easy way to remember hexadecimal is that many memory addresses start with `0x` or the simple mnemonic of *box*:

| Syntax: | Numeric base:         | Example: |
| ------- | --------------------- | -------- |
| `0b`    | Binary (base-2)       | `0b1010` |
| `0o`    | Octal (base-8)        | `0o70`   |
| `0x`    | Hexademical (base-16) | `0x2AF`  |

While not specifically mentioned in the Python Essentials 1 notes, it's worth knowing that *by default Python 3 outputs to standard Decimal (base-10) when performing calculations in different numerical bases.* However, there are the `bin()`, `oct()` and `hex()` functions which maintain the chosen notation:

`>>> print(0b1 + 0b1)`

`2`

`>>> print(bin(0b1 + 0b1))`

`0b10`

## Underscores in integers and floats

Python (apparently since Python 3.6) supports using underscores (_) as a substitute for commas for breaking up large integer and float variables such as 100,000 being represented as `100_000`. With strings, obviously, the underscore is part of the string.

`print(100_000)`

`100000`

`print("100_000")`

`100_000`
