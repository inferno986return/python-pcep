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

`print(0b1 + 0b1)`

`2`

`print(bin(0b1 + 0b1))`

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

### Exponentiation

Exponentiation is the formal mathematical term for multiplying a value by itself several times. In British English, we usually say "x to the power of y".

* **Exponentiation** (`**`) is two asterisks put together. For example, `2 ** 2` will output `4`.

Exponentiation is notably the *only operator which is right-side bound by default* though this can be overridden by using brackets.

`print(2 ** 2 ** 3)`

`256`

However, we can force left-side binding by using brackets:

`print(( 2** 2) **3)`

`64`

Lastly, we have literal exponentiation using the letter `E` for expressing very large (or small numbers) such as 2×10<sup>8</sup> (200,000,000), which would be `2E8` with this notation.

`print(2E8)`

`20000000.0`

Using an exponential with `E` creates a float value. Though as usual this can be forced into an integer by using `int()`.

### Left-side and right-side binding

The operators in Python are by default left-side bound except exponentiation.

### Division `/`, floor division `//` and modulo `%`

Python has three built-in forms of division:

1. **Division** (`/`) is the standard division operator which will *always* output a float value. For example, `9 / 3` will output `3.0`
2. **Floor division** (`//`) creates an integer by rounding the output to the lowest number and then removing all the values beyond the decimal point. For example, running floor division on these outputs `3` each time: `3.1`, `3.5`, `3.9`
3. **Modulo** (`%`) gives the remainder of a division as an integer. It can be useful for checking divisibility i.e. whether 9 is divisible by 3 or determining if a value is even.

Modulo can be manually calculated with these steps. For example, let's try `2 % 5`:

1. Divide the dividend (first number, two `2`) and divisor (second number, five `5`) normally `2 // 5`. All decimal quotients less (results) are rounded to the nearest integer – zero `0` in this case.
2. Multiply the quotient (zero `0`) by the divisor (five `5`), `0 * 5 ` (which is zero `0`)
3. Subtract the result from the original dividend, `2 - 0` (which is two `2`)
4. The remainder is two `2` in this example.


In summary, division always outputs floats and both floor division and modulo always output integers

If it's easier, you could refer to them as *float division* and *integer division* respectively. Ceiling division is the opposite of floor division, but there's no built-in operator for it and it is outside the scope of the PCEP.

It may also be outside the scope of the PCEP, but you may as well know the terminology: dividend / divisor = quotient

* The **dividend** is the number that is being divided. It represents the total amount that you are splitting into equal parts.
* The **divisor** is the number by which you are dividing the dividend. It represents the number of equal parts you are creating.
* The **quotient** is the result of the division. It represents the size of each equal part you obtain after dividing the dividend by the divisor.

See also: https://www.mathsisfun.com/numbers/division.html

And finally, division by zero is mathematically undefined. Therefore it will throw an error if you try to use zero (`0`) as the divisor:

`3 / 0`

`Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero`

### Variables

Like many interpreted programming languages, Python uses **dynamic variables** which means a variable's datatype is defined by the value itself rather than specific datatype keyword designation. 

Python variables are *case-sensitive* which means that `y = 1` and `Y = 2` can technically co-exist in the same block of code together while meaning different things:

`y = 0`

`Y = 1`

`print(y, Y)`

### Variable datatypes

For the PCEP, these datatypes are the only ones covered though there are many more built into Python 3:

* Integer – whole numbers such as `1`, `10` and `100`
* Float – decimal numbers such as `1.0`, `.5` and `1.23`
* String – a character or series of characters using single (`'`) or double (`"`) quotes such as `"Hello"`, `10` and `"This is a sentence."`
* Boolean – either `True` or `False` (booleans are case-sensitive)
