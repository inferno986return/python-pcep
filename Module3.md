# Python Essentials 1 – Module 3: Data Collections (Tuples, Dictionaries, Lists, and Strings)

## Section 3.2

### `break` and `continue` statements
The `break` and `continue` statements are designed to exit loops and skip loop interations respectively.

#### `break` statement
`break` will abruptly and prematurely exit the loop (like Ctrl+C does in the terminal). In a nested loop, the parent loop will still keep running unless that also has a `break` or meets its condition. 

Note that `break` will also ignore any `else` statements used by the loop which usually run when the loop has met its condition.

For nested loops, `break` will exit the inner loop that it is used in.

#### `continue` statement
`continue` skips an interation of a loop.

In this example, odd numbers are printed to the console:

```
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```
```
1
3
5
7
9
```

### LAB 22: Collatz conjecture
Collatz conjecture is an unsolved yet simplistic mathematical problem and the second lab exercise for while loops. For the sake of this Python lab, we assume that every c0 is a positive integer (that isn't zero) and with enough steps it can be made equal to 1.

The steps for Collatz conjecture are as follows, as per Wikipedia:

1. Take a positive integer which is greater than or equal to 1 and label it as c0.
2. For even numbers, divide c0 by 2;
3. For odd numbers, multiply c0 by 3 and add 1.
4. With enough repetition, do all positive integers converge to 1?

The PCEP example provided for `c0 = 15` might be incorrect and I have informed the Python Institute. Anyway, here's my output:

`Enter a number for c0:15`

`46`

`23`

`70`

`35`

`106`

`53`

`160`

`80`

`40`

`20`

`10`

`5`

`16`

`8`

`4`

`2`

`1`

`steps = 17`

This lab wasn't particularly difficult if you understand while loops, if statements, incrementation and the modulo `%` operator. Here's my source code which I tried to write more elegantly that with my first attempt:

```
c0 = int(input("Enter a number for c0:"))
steps = 0

while c0 != 1:

    if c0 % 2 == 0:
       c0 = c0 // 2
       steps += 1
       print(c0)

    elif c0 % 2 != 0:
       c0 = c0 * 3 + 1
       steps += 1
       print(c0)

print(c0)
print(f"Steps = {steps}")
```

# Section 3

## Logical expressions

In electronics, there are logic gates which take inputs and produce different outputs. In the PCEP, you need to know these four: AND, OR, XOR NOT

>  Wiktionary defines **conjuction** as: (logic) The proposition resulting from the combination of two or more propositions using the `∧` operator.

AND is a conjunction, all inputs must be a `1` to get an output of `1`, as per the truth table below:

<!--diagram-->

| Input A | Input B | Output |
| ------- | ------- | ------ |
|   `0`   |   `0`   |   `0`  |
|   `1`   |   `0`   |   `0`  |
|   `0`   |   `1`   |   `0`  |
|   `1`   |   `1`   |   `1`  |

> Wiktionary defines **disjunction** as: (mathematics) A logical operator that results in “true” when some of its operands are true.

OR is a disjunction and it is flexible. If at least 1 input is a `1` then the output will be `1`. See the truth table below:

<!--diagram-->

| Input A | Input B | Output |
| ------- | ------  | ------ |
|   `0`   |   `0`   |   `0`  |
|   `1`   |   `0`   |   `1`  |
|   `0`   |   `1`   |   `1`  |
|   `1`   |   `1`   |   `1`  |

XOR is exclusive OR which means one or the other, but not both making it the opposite of AND. As a fun fact, XOR is used for the parity bit in RAID 5 setups to verify data integrity. See the truth table below:

<!--diagram-->

| Input A | Input B | Output |
| ------- | ------  | ------ |
|   `0`   |   `0`   |   `0`  |
|   `1`   |   `0`   |   `1`  |
|   `0`   |   `1`   |   `1`  |
|   `1`   |   `1`   |   `0`  |

NOT simply flips the output from `0` to `1` and vice-versa. In electronic engineering, the NOT gate is called an *inverter* as it will invert the output. Usually, it's combined with other logic gates to make: NAND, NOR and NXOR. As a fun fact, NAND gates are the basis for solid-state storage used in flash drives and solid-state drives (SSDs).

Using NOT NOT results in a double negative effect similar to statements made in English such as: *"I will not not leave the house today"*. Also, using two minus signs together negates them into a plus `1 -- 1 = 2`

| Input A | Output |
| ------- | ------ |
|   `0`   |   `1`  |
|   `1`   |   `0`  |

### Boolean order of operations

Much like how mathematical operators use `PEMDAS`, logical operators are also evaluated in a fixed order. You could use the mnemonic `NAXO`:

1. **N**OT
2. **A**ND
3. **X**OR
4. **O**R

## Bitwise operations

The Boolean logic operators in Python only compare the whole integers. However, the separate bitwise operators allow comparison of the individual binary digits (bits) that comprise the integer.

### Bitwise NOT (`~`)

Bitwise NOT (`~`) is represented using a tilde symbol and flips the bits of an integer. Let's use decimal `5` as an example:

| 8 | 4 | 2 | 1 |
|---|---|---|---|
|`0`|`1`|`0`|`1`|

From adding `1 + 4 = 5`, so that's nice and easy. Now to flip it which is called One's compliment:

| 8 | 4 | 2 | 1 |
|---|---|---|---|
|`1`|`0`|`1`|`0`|

Add a bit to the right column:

| 8 | 4 | 2 | 1 |
|---|---|---|---|
|`1`|`0`|`1`|`1`|

### Two's complement
> Probably cheating, but I find for integers (`i`) you can use a minus (`-`) and then add 1. Such as: `~1 = -2`, `~3 = -3`, `~4 = -4`

Two's complement is the standard form for representing signed numbers in binary. All Python integers are signed, meaning they use a sign bit on the furthest left column to represent positive (`0`) and negative (`1`) numbers. To represent binary, we need at least 4 bits (i.e. a nibble) and start with decimal `7`:

| - | 4 | 2 | 1 |
|---|---|---|---|
|`0`|`1`|`1`|`1`|

Positive integers are easy! Just add up the bits, the equivalent Python:

`print(bin(7))`

`0b111`

For negative integers, it gets tricky and we need to perform some steps to get `-7` decimal:

1. Convert to one's complement, this means flipping the bits which is the bitwise NOT (`~`) operation.

| - | 4 | 2 | 1 |
|---|---|---|---|
|`1`|`0`|`0`|`0`|

2. Add one to the right-most column. In this case, the binary addition is `0 + 1 = 1`.

| - | 4 | 2 | 1 |
|---|---|---|---|
|`1`|`0`|`0`|`1`|

These are the key rules for binary addition:

1. `0 + 0 = 0`
2. `0 + 1 = 1`
3. `1 + 0 = 1`
4. `1 + 1 = 0` (with a carry-over of 1 to the next bit to the left)

3. Re-add the sign bit?

Examples in the PCEP and elsewhere prefer to use 32-bit signed integers when demonstrating two's compliment. In reality, Python has dynamic variables and integer capacity can theoretically be as large as the RAM of the computer running the interpreter allows.

### Working with single bits within an integer

Bitwise operators make it possible to alter individual bits within an integer. For example, let's take the hexadecimal value `0x1234` (decimal `4660`) and assign it to the variable `flag_register`:

`flag_register = 0x1234`

Each bit is effectively its own boolean value (i.e. each binary number is either true or false). We only care about the 3rd digit from the right (marked with the `y`):

`flag_register = 1001000110y00`

Let's check the digit's status (i.e. whether it's a `0` or `1`) by using bitwise AND (`&`) to create a "bit mask" which isolates individual bits within a binary number. We can define the position we want by using exponentiation, which is nice and simple:

> "No one cared who I was until I put on the mask." — Bane, The Dark Knight Rises (2012)

```
the_mask = 2**3  # Creates a mask with a 1 at the 3rd bit position (weight of 2^3)

if flag_register & the_mask:
    print("My bit is set (1)")
   
else:
    print("My bit is reset (0)")
```

In this example, we get an `8` which means there is a `1` on the 3rd position:

### Bit shifting left (`<<`) and right (`>>`)
>TL;DR: Bit shifting moves the bits around to make the number larger or smaller. Fortunately, there are simple formulae for calculating them so you don't have to carry a lot of bits when performing binary addition.

Shifting moves the bits of an integer to enlarge it or make it smaller.

Bitwise left shifting `<<` shifts all bits in a number to the left by a specified number of positions. It can be calculated using the formula: `x << y = x * y ** y`

`print(4 << 2) # 4 * (2 ** 2)`

`16`

Conversely, bitwise right shifting `>>` shifts all bits in a number to the right by a specified number of positions. It can be calculated using the formula (I've used floor division to force an integer) - `x << y = x // y ** y`

`print(4 >> 2) # 4 // (2 ** 2)`

`1`


### Compare boolean and bitwise operations

Let's start by assigning two variables `i` and `j`:

```
i = 15
j = 22
```

Now assuming these variables are 32-bit integers, their binary values will be as follows:

```
i: 00000000000000000000000000001111
j: 00000000000000000000000000010110
```

Now let's Boolean AND them together:

`log = i and j`

By default, if we combine the two we get decimal `22` or binary `0b10110`. However, if we force the output as a boolean, we get True:

`print(bool(log))`

`True`

This output is to be expected from the AND truth table from earlier. By default, Python will usually treat zero `0` as False and other integers as True.

Next, we have bitwise:

`bit = i & j`

## Lists

A list is a collection of values (usually integers or strings) as a single variable datatype: For example, let's start with an empty list by denoting it with square brackets `[]`:

`my_list = []`

Then fill it with some simple integer values:

`my_list = [1,2,3,4,5]`

Python lists are heterogeneous, which means that almost any datatype can be inserted as an item into a list (even other lists, which are called nested lists). However, for the PCEP examples, the lists comprise of integers:

`mixed_list = [True, 1.0, 2, "This is a string."]`

elements within a list can be referenced using an index in square brackets. Remember that lists count from zero, so `[0]` is the first item within a list variable.

`print(my_list[1])`

`2`

But using a minus starting from `[-1]`, index counts the list elements from right to left, for example:

`print(my_list[-1])`

`5`

Confusingly, Python will ignore the minus `-` in `[-0]` as an index and just return the first element from left to right:

`print(my_list[-0])`

`1`

### List variables are referenced
An interesting feature of Python lists is that are referenced in memory when assigned (like how pointers in C will *point* to the memory address of the variable rather than the variable itself) and therefore behave differently to integers and floats. So if you assign a list to another variable, if the original list gets updated then so will the other:

```
list1 = [0]
list2 = list1
list1[0] = 2

print(list2)
```

The output here is `2` as the original list was modified and `list2` merely references `list1`.

### List slicing

List slicing allows the duplication and manipulation of lists by defining the elements using their index and a colon `:`. Let's start with a simple list with a slice of `[1:3]`:

```
list = [0,1,2,3,4,5]
list2 = list[1:3]
print(list2)
```
`[1, 2]`

With slice `[1:3]`, the output will take indices (plural of index) `1` and `2`. Much like the `range()` the end index is always one less than the number specified.

#### Negative list indices

Using a negative index number in the slice as the start will empty the list to `[]`, such as `[-1:1]`. Using a negative index as the end value will remove elements from right to left such as `[1:-]`. Just using `[-1:]` will remove all the elements from the list except the last element.

#### List duplication

Using a slice without indices `[:]` encompasses all the elements and creates a duplicate of the list. Merely assigning a list to a variable creates a reference as mentioned earlier:

```
list = [0,1,2,3,4,5]
list2 = list[:]
print(list2)
```
`[0, 1, 2, 3, 4, 5]`

However, I question the practical usage of this slice, as the same effect can be achieved without the slice `[:]` by using the more efficient `copy()` method, especially for larger lists with a lot of elements. Though the `copy()` method isn't mentioned in the PCEP notes:

```
list = [0,1,2,3,4,5]
list2 = list.copy()
print(list2)
```
`[0, 1, 2, 3, 4, 5]`

#### Using list slices and `del`

`del` is pretty flexible and it's efficient too. It will purge elements from memory, which is important for large and complicated Python programs. List elements can be bulk deleted by referencing them in a slice:


It can also delete all the elements in a list by using the colon slice `[:]` leaving just an empty list:

#### LAB: Operating with lists ‒ basics

This was a tricky lab, though I found a solution that uses slices to `my_list` to check for duplicate elements, creates a temporary tidied-up list, uses the tidied-up list as the new `my_list` and then finally deletes the `tidied_list` as it's unneeded.

The cheat way to do this is to convert the list to a set which will automatically remove duplicates (sets do not allow duplicate elements), then back to a list.

```
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# my_list = set(my_list)
# my_list = list(my_list)

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
tidied_list = []

for i in range(len(my_list)):
  if my_list[i] not in my_list[i+1:]:  # Check if element is in remaining list
    tidied_list.append(my_list[i])

my_list = tidied_list[:]
del tidied_list

print(my_list)  # Output: [1, 2, 4, 6, 9]


print("The list with unique elements only:")
print(my_list)
```

