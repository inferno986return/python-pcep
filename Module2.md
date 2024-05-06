# Python Essentials 1 – Module 2: Python Data Types, Variables, Operators and Basic I/O Operations

## Section 2.1: The "Hello World! program
### Printing "Hello World"
`print()` is an important built-in function in Python as it allows an easy way to output data to the console. In Python 3, `print()` is built into the language itself and can take no arguments, where it only prints a blank line.

**Tip:** In Python 2, `print` was a statement instead of a function.

When learning a programming language, it's common to start by outputting "Hello World" by using the built-in print function. So for Python 3, this can be done on a single line:

```
print("Hello World")
```
```
Hello World
```

The use of single quotes `'` or double quotes `"` is used to define a string variable which holds `"Hello World"`.

By default, each `print()` statement automatically adds a newline `\n` character to separate outputs:

```
print("Hello")
print("World")
```

This outputs the following:

```
Hello
World
```

It is possible to print multiple outputs at once by using a comma `,` between them, in this case `"Hello"` and `"World"` are two separate strings: 

```
print("Hello", "World")
```
```
Hello World
```

The comma will add a space between the variables and keep them on one line as the newline `\n` is at the end of the `print()` function, at least by default. Let's try outputting `"Hello"` and `"World"` over separate lines, but using only one `print()` function:

```
print("Hello\nWorld")
```

```
Hello
World
```

We can also use a tab `\t` to indent the output like so:

```
print("\tHello World")
```

```
    Hello World
```

### The 4 parameters of the `print()` function

**Tip:** You will need to know the definitions of and differences between these three terms for the Python PCEP exam:

Within the brackets of a function such as `print()`, a **parameter** is the placeholder for the function's arguments and **arguments** are the actual values passed to the function. When using a parameter with an equals sign `=`, these are called **keyword arguments** and can specified in any order. 

The `print()` function supports 4 keyword arugments which are `sep`, `end`, `file` and `flush`. However, for the Python PCEP we are only concerned with both `sep` and `end`. The parameters `sep=` and `end=` can be optionally used after defining the outputs for a `print()` function to alter the output. Let's start with `sep=`.

By default, the value of `sep` is a space to separate the outputs of the `print()` function, equivalent to `sep=" "`. The initial Hello World program we wrote would look like this and you'll notice there is no difference in the output:

```
print("Hello World", sep=" ")
```

`Hello World`

If you define `sep` with something else it will replace the *default use of a space* between outputs with a character of your choice such as a hypthen `-` or an asterisk `*`:

```
print("Hello","World",sep="-")
```

`Hello-World`

By default,`end` uses a newline `\n` to define the end of the line used by the `print()` function. Going back to our first Hello World program, it would look like this and you'll notice the output is also unchanged:

```
print("Hello World", end="\n")
```

`Hello World`

With this example, the `end` parameter has been defined without any arguments.

```
print("Hello",end="")
print("World")
```
```
HelloWorld
```

With this example, the two strings have just concatenated together to form one simple output using CamelCase. 

Note that the keyword `sep=` and `end=` are defined at the end of the `print()` function declaration otherwise you'll get a syntax error:

```
print(sep="7", "Hello", "World")
```
```
File "<stdin>", line 1
    print(sep="7", "Hello", "World")
                                   ^
SyntaxError: positional argument follows keyword argument
```

The keyword arguments can be defined in any order as long as they are after the function's arguments. Such as:

```
print("Hello", "World", end=".", sep="-")
```
```
Hello-World.
```

**Advanced learning:** The other two keyword arguments for `print()` are `file` which can save the output of the `print()` function to a file and `flush` which is a Boolean value (i.e. `True` or `False`) that clears the output after a new `print()` output has been written. By default, the value of `flush` is `False`.

### Printing formatted string literals (f-strings)

While not part of the PCEP syllabus, starting from Python 3.6 you can use formatted string literals (f-strings) which are an elegant way to print variable values along with a string by specifying the variables using curly braces `{}`:

```
apples = 2
bananas = 3

print(f"Jim has {apples} apples and {bananas} bananas.")
```

Without an f-string, we have to break up the output and add spaces to the strings which looks messy and less human-readable:

```
apples = 2
bananas = 3

print("Jim has ", apples, " apples and ", bananas, " bananas.")
```

Or alternatively, you could use the plus `+` operator instead of commas `,`:

```
apples = 2
bananas = 3

print("Jim has " + apples + " apples and " + bananas + " bananas.")
```

## Section 2.2: Python literals

A literal is a variable where the human can easily determine its value from the datatype.

### Underscores in integers and floats

Python (apparently since Python 3.6) supports using underscores (_) as a substitute for commas for breaking up large integer and float variables such as 100,000 being represented as `100_000`:

`print(100_000)`

`100000`

**Tip:** This underscore notation for integers and floats is purely cosmetic to provide human readability and doesn't affect the value.

However, for strings the underscore is part of the string:

`print("100_000")`

`100_000`

### Binary, Octal and Hexadecimal
//Could explain numeric bases

Binary, octal and hexadecimal numbers can be represented as **literals** using this notation. An easy way to remember hexadecimal is that many memory addresses start with `0x` or you can just use the simple mnemonic of *box*:

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

Exponentiation is notably the *only default operator which is right-side bound by default* though this can be overridden by using brackets.

```
print(2 ** 2 ** 3)
```
```
256
```

Which is equivalent to:

```
print(2 ** (2 ** 3))
```
```
256
```

However, we can force left-side binding by using brackets:

`print((2 ** 2) ** 3)`

`64`

You may have realised this is the same as 2<sup>8</sup> (2^8 = 2×2×2×2×2×2×2×2)

Lastly, we have literal exponentiation using the uppercase letter `E` (or lowercase letter `e`) for expressing very large (or very small) numbers such as 200 million (2×10<sup>8</sup> = 200,000,000), which would be `2E8` with this notation.

`print(2E8)`

`20000000.0`

A more practical example would be Avrogadro's constant which is used in chemistry. However, in real life I would recommend using an external library like Scipy or Astropy for this:

`avogadro_number = 6.02E23  # 6.02 x 10^23`

Much like division `/`, using an exponential with `E` creates a float value. Though as usual this can be forced into an integer by using `int()`.

### Left-side and right-side binding

The operators in Python are by default left-side bound with the only exception being exponentiation `**`. This means that calculations are performed from left-to-right:

`2 - 1 + 3`

`4`

This is despite the PEMDAS order being addition first and then subtraction. Brackets `()` can be used to override left-side binding and force a particular order if that is required.

### Three ways to divide – Division `/`, floor division `//` and modulo `%`

You may as well know the terminology for division as I use it extensively in this section: dividend / divisor = quotient

* The **dividend** is the number that is being divided. It represents the total amount that you are splitting into equal parts.
* The **divisor** is the number by which you are dividing the dividend. It represents the number of equal parts you are creating.
* The **quotient** is the result of the division. It represents the size of each equal part you obtain after dividing the dividend by the divisor.

See also: https://www.mathsisfun.com/numbers/division.html

Python has three built-in forms of division:

1. **Division** (`/`) is the standard division operator which will *always* output a float value. For example, `9 / 3` will output `3.0`.
2. **Floor division** (`//`) creates an integer by rounding the output to the lowest number and then removing all the values beyond the decimal point. For example, running floor division on these outputs `3` each time: `3.1`, `3.5`, `3.9`
3. **Modulo** (`%`) gives the remainder of a division as an integer. It can be useful for checking divisibility i.e. whether 9 is divisible by 3 or determining if a value is even (divisible by 2).

Modulo can be manually calculated with these four steps. For example, let's try `2 % 5`:

1. **Divide the dividend** (the first number, two `2`) and divisor (the second number, five `5`) normally `2 // 5`. All decimal quotients (results) are rounded to the nearest integer – zero `0` in this case.
2. **Multiply the quotient** (zero `0`) by the divisor (five `5`), `0 * 5 ` (which is zero `0`).
3. **Subtract the result** from the original dividend, `2 - 0` (which is two `2`).
4. The **remainder** is two `2` in this example.

Try a few practice problems on paper to get the hang of it. You can also refer to and test this sample function I made:

```
def modulo(x, y):
    z = x // y # Divide as usual, but force an integer
    m = z * y # Multiply the quotient by the divisor
    r = x - m # Subtract the dividend to find remainder
    return r

x = int(input("x: "))
y = int(input("y: "))
print("Remainder:", modulo(x, y))
print("Should be:", x % y)
```

Alternatively, a quick and lazy way is to estimate the remainder for some modulo problems is just dividing the dividend and devisor in your head and use the nearest multiple. This only works for me where the *dividend is larger than the divisor*. So instead of `2 % 5`, I can do `11 % 4` and since 4×3=12, the remainder can be guessed as 3.

**Exam tip:** For the Python PCEP exam, you will need to remember that division `/` always outputs a **float** value and both floor division `//` and modulo `%` always output an **integer** value.

If it's easier, you could refer to them as *float division* and *integer division* respectively. 

**Beyond the PCEP:** Ceiling division is the opposite of floor division, but there's no built-in operator for it and instead there is a function avilable in the built-in `math` library, but this is outside the scope of the PCEP.

And finally, **division by zero** is mathematically undefined. Therefore it will throw a `ZeroDivisionError` error if you try to use zero (`0`) as the divisor in calculation which will stop the program execution by default:

`3 / 0`

`Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero`

This also applies to floor division `//` where the divisor is a decimal number such as `0.25` or `0.5`.

In a later module, we discuss how to manage exceptions including dividing by zero errors to keep the program running. 😀

### Variables

Like many interpreted programming languages, Python uses **dynamic variables** which means a variable's datatype is defined by the value itself rather than specific datatype keyword designation.

Python variable names are *case-sensitive* which means that `y = 1` and `Y = 2` can technically co-exist in the same block of code together while meaning different things. However, this can still cause unnecessary confusion to a human programmer:

```
y = 0
Y = 1

print(y, Y)
```

`0 1`

### Variable datatypes

For the PCEP, these are the only datatypes that are covered and you'll need to know for the exam. However, though there are many more built into Python 3:

* **Integer** – whole numbers such as `1`, `10` and `100`
* **Float** – decimal numbers such as `1.0`, `.5` and `1.23`
* **String** – a character or series of characters using single (`'`) or double (`"`) quotes such as `"Hello"`, `"10"` and `"This is a sentence."`
* **Boolean** – either `True` or `False` (booleans are case-sensitive)

These are covered in much more detail in later modules:

* **List** – a collection of values of any datatype in any order and with duplicates (very flexible): `[0,1,2,3,4,5,"potato",True]`
* **Tuple** – an immutable ordered collection of variables with no duplicate values such as: `(1,2,3,4,5, "apple")`
* **Dictionary** – a collection of key:value pairs, similar to a list. Since Python 3.6, they are ordered by default and no longer randomised: `["sandwich:chicken","drink:orange_juice","soup:tomato"]`
* **`None`** – an empty value equivalent to `NULL` in other programming languages. Technically, it is a datatype of its own which is returned by all functions that have no `return` statement.

## 3.1 Making decisions in Python

If statements allow conditional branching. Each `if` statement is evaluated seperately

`elif`

Let's go back to my source code for the Collatz conjecture lab. I found by accident that by using two separate `if` statements this would create an infinite loop as each condition is evaluated separately.

```
c0 = int(input("Enter a number for c0:"))
steps = 0

while c0 != 1:

    if c0 % 2 == 0:
       c0 = c0 // 2
       steps += 1
       print(c0)

    if c0 % 2 != 0:
       c0 = c0 * 3 + 1
       steps += 1
       print(c0)

print(c0)
print(f"Steps = {steps}")
```