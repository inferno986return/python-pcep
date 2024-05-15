# Cisco SkillsForAll PCEP Practice Test
## Current score 46% out of 75% – 61.33% of the way there!

### Question 1: What is the output of this code snippet?

```
my_list = [1, 2]
 
for v in range(2):
    my_list.insert(-1, my_list[v])
 
print(my_list)
```

Possible answers:

**A. [1, 1, 1, 2]**

B. [2, 1, 1, 2]

C. [1, 2, 1, 2]

D. [1, 2, 2, 2]

I ran this code snippet, but why is the answer A? I am convinced it was C. The loop uses the iterator `v` with the `list.insert()` method to add elements just before the final element of the list `2`.

1. First Iteration (`v = 0`):
* `my_list[v]` is `1`.
* `my_list.insert(-1, my_list[v])` inserts 1 at the second-to-last position.
* Now, `my_list` becomes `[1, 1, 2]`.

2. Second Iteration (`v = 1`)`:
* `my_list[v]` is now `1` (since `my_list` has been modified in the first iteration).
* `my_list.insert(-1, my_list[v])` inserts `1` at the second-to-last position again.
* Now, `my_list` becomes `[1, 1, 1, 2]`.

So, after the loop, my_list is `[1, 1, 1, 2]`, not `[1, 2, 1, 2]`.

The key point here is that *the list is being modified while it’s being iterated over, which affects the result* of `my_list[v]` in the second iteration. The `insert(-1, ...)` method call shifts the last element (`2`) further to the right each time an insertion is made, resulting in the final list having three 1s before the `2`.

I also hadn't factored in that the `insert()` method will insert elements before the index specified.

### Question 2: The meaning of a positional argument is determined by:

A. its connection with existing variables

**B. its position within the argument list** 

C. the argument’s name specified along with its value

D. its value

The term *positional argument* reveals the answer, it's really that simple! For example, in the function `example(a,b)` the paramers are `a` and `b`, but the values they represent have to be in the defined order which are positional arguments.

### Question 3: Which of the following sentences are true about the code? (Select two answers)

```
nums = [1, 2, 3]
vals = nums
```

**A. nums has the same length as vals**
B. nums and vals are different lists
C. vals is longer than nums
**D. nums and vals are different names of the same list**

Lists are unusual as when they are assigned to other variables like this they are merely referenced, so `nums` and `vals` are the same list. This means that if `nums` changed in any way, `vals` would also be affected. Either a slice (`nums = vals[:]`) or method (`nums = vals.copy()`) would need to be used to make `nums` a separate duplicate list.

### Question 4: An operator able to check whether two values are not equal is coded as:

**A. `!=`**

B. `=/=`

C. `not ==`

D. `<>`

Another easy question! `!=` is the only not equal symbol (at least in this list) that is recognised by Python 3 and a common programming symbol overall. 

**Advanced learning:** At least two of these operators can be used in other programming languages, just not Python 3. `=/=` is used in Erlang as the "Exactly not equal to" operator and `<>` can be used in some SQL and BASIC dialects to represent not equal to.

### Question 5: What is the output of this code snippet?

```
def function_1(a):
    return None
 
 
def function_2(a):
    return function_1(a) * function_1(a)
 
 
print(function_2(2))
```

A. will output `4`
B. will output `2`
C. will output `16`
**D. will cause a runtime error**

The key is that `None` was returned by `function_1()`. `None` is Python 3's counterpart to `NULL` which is an empty value so it cannot be multiplied (though it can be compared such as `x == None`). This is yet another example of devious PCEP code since all functions without a `return` statement automatically return `None`.

```
line 6, in function_2
    return function_1(a) * function_1(a)
           ~~~~~~~~~~~~~~^~~~~~~~~~~~~~~
TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'
```

### Question 6: What is the result of the following division?

```
1 // 2
```

A. is equal to 0.5
B. cannot be predicted
**C. is equal to 0**
D. is equal to 0.0

This one is also very easy as it's a simple floor division operation so `1 // 2 = 0`. Floor division will *only output integers* or a `DivideByZeroError` in the case the divisor is zero `0`.

### Question 7: What is the output of the following snippet:

```
def func(a, b):
    return b ** a
 
 
print(func(b=2, 2))
```

**A. is erroneous**
B. will output `2`
C. will output `4`
D. will output `None`

The order of positional arguments does matter, so the Python 3 interpreter won't allow this `print()` function and subsequently generates a `SyntaxError`.

```
line 5
    print(func(b=2, 2))
                     ^
SyntaxError: positional argument follows keyword argument
```

However, this can be fixed by swapping the positional arguments to `print(func(2, b=2))` which outputs `4`.

### Question 8: What value will be assigned to the `x` variable?

```
z = 0
y = 10
x = y < z and z > y or y < z and z < y
```

**A. `False`**
B. `1`
C. `True`
D. `0`

This was a tricky one for me and I initially got this incorrect as `True`. Remember `NAXO` which is the Boolean algebra order of operations, this means the `and` comparisons happen first and then `or` comparison with these 4 steps: 

1. `(y < z and z > y) or (y < z and z < y)`
2. `(False and False) or (False and True)`
3. `False or False`
4. `False`

### Question 9: Which of the following variable names are illegal and will cause the SyntaxError exception? (Select two answers)

**A. for**
**B. in**
C. print
D. In

`for` and `in` are reserved keywords in Python 3, using them as variables will result in a `SyntaxError`. As for the other answers, Python 2 used to reserve `print` as a statement, though since becoming a built-in function this restriction was dropped. Also since Python 3 is case-sensititive `In` is technically allowed. I wouldn't recommend using either `print` or `In` as variable names though as it may add unneccessary complexity to your source code.

### Question 10: What is the output of the following snippet?

```
my_list = [x * x for x in range(5)]
 
 
def fun(lst):
    del lst[lst[2]]
    return lst
 
 
print(fun(my_list))
```

A. `[1, 4, 9, 16]`
B. `[0, 1, 9, 16]`
**C. `[0, 1, 4, 9]`**
D. `[0, 1, 4, 16]`

I got this one incorrect too. Looking at the possible answers does at least give a hint, so the initial `my_list = [0,1,4,9,16]` as `range(5)` generates the numbers from 0 to 4 using *list comprehension* (defining a list's elements based on a formula rather than using individual literals). 

Be careful with those nested list indicies for the `del` statement as it goes to the 2nd element of the list `4` and then uses that index to delete the 4th element `16`. Work your way outwards from a nested index.

### Question 11: What is the output of the following piece of code?

```
x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z
 
print(x, y, z)
```

A. `2 1 2`
**B. `1 1 2`**
C. `1 2 2`
D. `1 2 1`

This is another piece of devious PCEP code. The important thing to remember is the `1 1 2` and the key is to follow the variable values as they are assigned from right to left.

### Question 12: What will be the output of the following snippet?

```
a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b
 
print(a, b)
```

**A. `0 1`**
B. `1 1`
C. `0 0`
D. `1 0`

The answer is `0 1` but I didn't get that correct. I first mistook the caret `^` which means bitwise XOR for bitwise AND whch uses the ampersand `&`. Then I didn't consider the two bits which comprise the variables `a = 01, b = 00`, then `a = 01 ^ 00` sets `a = 1`, same for `b = 01 ^ 00` sets `b = 1` therefore `a = 01 ^ 01` sets `a` back to zero (0) as they have identical inputs.

To make it even simpler as this is just comparing one bit:

```
a = 0
b = 1
```

1. `a = a ^ b`, therefore `1 = 1 ^ 0`
2. `b = a ^ b`, therefore `1 = 1 ^ 0`
3. `a = a ^ b`, therefore `0 = 1 ^ 1`
4. `print(a,b)`, outputs: `0 1`   

### Question 13: What is the output of the following snippet?

```
def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2
 
 
print(fun(fun(2)))
```

A. `1`
B. the code will cause a runtime error
C. `2None`
**D. `2`**

The output is `2`, so I got this one correct! This is a simple recursive function.

### Question 14: Take a look at the snippet and choose the true statement.

```
nums = [1, 2, 3]
vals = nums
del vals[:]
```

**A. `nums` and `vals` have the same length**
B. `vals` is longer than `nums`
C. `nums` is longer than `vals`
D. the snippet will cause a runtime error

As mentioned previously in question 3, `vals` is the same list as `nums`, in the C language there is a concept of pointers which point to (reference) the area of memory where a variable is contained.

### Question 15: What is the output of the following piece of code if the user enters two lines containing 3 and 2 respectively?

```
x = int(input()) # 3
y = int(input()) # 2
x = x % y
x = x % y
y = y % x
print(y)
```

**A. 0**
B. 2
C. 1
D. 3

I thought it was `1` or `2`, but the answer is zero `0`. This is because the `y` assigment is `2 % 1 = 0`

Modulo reveals the remainder of a division rather than the quotient. For all natural numbers (integers above zero) `n`, `n mod 1 = 0` in every case because every natural number is divisible by `1` (some are only divisible by one and themselves hence they are prime numbers).

### Question 16: What is the output of the following piece of code if the user enters two lines containing 3 and 6 respectively?

```
y = input() # "3"
x = input() # "6"
print(x + y)
```

**A. `63`**
B. `36`
C. `3`
D. `6`

Yikes I got this one incorrect too as I didn't pay attention to the order of `x` and `y`.

Read over the code to ensure you haven't missed anything.

### Question 17: What is the output of the following piece of code?

```
print("a", "b", "c", sep="sep")
```

A. `a b c`
**B. `asepbsepc`**
C. `abc`
D. `asepbsepcsep`

Well I got this one correct as `sep` goes in between the outputs.

### Question 18: What is the output of the following piece of code?

```
x = 1 // 5 + 1 / 5
print(x)
```

A. `0`
**B. `0.2`**
C. `0.4`
D. `0.5`

I got this one correct. Nice and simple, remember *PEMDAS* so `1 // 5 = 0`, `1 / 5 = 0.2` and `0 + 0.2 = 0.2`.

### Question 19: Assuming that my_tuple is a correctly created tuple, the fact that tuples are immutable means that the following instruction:

```
my_tuple[1] = my_tuple[1] + my_tuple[0]
```

A. is fully correct
**B. is illegal**
C. may be illegal if the tuple contains strings
D. can be executed if and only if the tuple contains at least two elements

Tuples are immutable adn therefore modifying it directly would lead to an error. Alternatively, you can create a new tuple and modify that.

### Question 20: What is the output of the following piece of code if the user enters two lines containing 2 and 4 respectively?

```
x = float(input()) # 2.0
y = float(input()) # 4.0
print(y ** (1 / x))
```

A. `4.2`
B. `1.0`
**C. `2.0`**
D. `0.0`

Nice and easy. `4.0` to the power of `0.5` is `2.0`. For square numbers `s` exponentition to `0.5` is the same as running a square root `math.sqrt()` operation on them, hence this formula: `sqrt(s) = s^0.5`. Does this apply to all square numbers?

### Question 21: What is the output of the following snippet?

```
dct = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dct['three']
 
for k in range(len(dct)):
    v = dct[v]
 
print(v)
```

A. `two`
B. `('one', 'two', 'three')`
**C. `one`**
D. `three`

This is `one` because `v` loops through the whole dictionary and goes back to the starting point due to using the dict's length as the range for the `for` loop.

### Question 22: How many elements does the lst list contain?

```
lst = [i for i in range(-1, -2)]
```

A. `three`
B. `two`
**C. `zero`**
D. `one`

This generates an empty list `lst = []` as the `range()` start is `-1` and the stop `-2`, as there are no integers between those values nothing is added to the list. But it's still a list and therefore needs the square brackets `[]` to be defined as one.

Remember for `range()` since there is no integer that satisfies the condition of being greater than -1 and less than -2 when counting by ones, the range is empty, and thus no -1 is included in the list.

### Question 23: Which of the following lines correctly invoke the function defined below? (Select two answers)

```
def fun(a, b, c=0):
    # Body of the function.
```

A. `fun(b=1)`
B.`fun()`
**C.`fun(0, 1, 2)`**
D. `fun(b=0, a=0)`

### Question 24: What is the output of the following snippet?

```
def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)
 
 
print(fun(0, 3))
``` 

A. the snippet will cause a runtime error
B. `2`
**C. `0`**
D. `1`

The recursive function `fun(0,3)` will keep running each time until `y` decrements down to zero `0` and is equal to `x` which is also zero `0`. Therefore zero `0` is returned and printed.

### Question 25: How many stars (*) will the following snippet send to the console?

```
i = 0
while i < i + 2 :
    i += 1
    print("*")
else:
    print("*")
```

A. zero
B. one
**C. the snippet will enter an infinite loop, printing one star per line**
D. two

Another deceptive question, but paying attention to the while loop condition shows this is an infinite loop with no exit condition so it can print an infinite number of stars with one per line.

### Question 26: What is the output of the following snippet?

```
tup = (1, 2, 4, 8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)
```

**A. 4**
B. 44
C. (4,)
D. (4)

I found this tricky, though the first slice `tup[-2:-1]` starts at `4` and ends in `8`. The start element is left over as the rest are sliced out making the single-element tuple `tup = (4,)` and then `tup[-1]` removes the tuple entirely leaving an integer, this also works for lists.

* Start Index: “Start slicing from here, and include this element.”
* End Index: “Stop slicing before this element.”

### Question Question 27: What is the output of the following snippet?

```
dd = {"1": "0", "0": "1"}
for x in dd.vals():
    print(x, end="")
```

A. 1 0
**B. the code is erroneous (the dict object has no vals() method)**
C. 0 1
D. 0 0

More devious code from PCEP. There is no `dict.vals()` method and this will output an attribute error, however, there is a `dict.values()` method which will output `01` with this code.

```
line 2, in <module>
    for x in dd.vals():
             ^^^^^^^
AttributeError: 'dict' object has no attribute 'vals'. Did you mean: 'values'?
```

### Question 28: What is the output of the following snippet?

```
dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)
 
for x in dct.keys():
    print(dct[x][1], end="")
```

A. (1,2)
B. 12
**C. 21**
D. (2,1)

Another tricky question, the key takeway is that the dict holds 2 tuples `(1,2)` and `(2,1)`, so 2 indices `[x][1]` are required to specify and print the second value of each tuple. The `end` ensures the two outputs concatenate together.

### Question 29: What is the output of the following snippet?

```
def fun(inp=2, out=3):
    return inp * out
 
 
print(fun(out=2))
```

A. `2`
B. `6`
C. the snippet is erroneous and will cause SyntaxError
**D. `4`**

I didn't get this one correct either, but it makes sense. The function `fun(inp=2, out=3)` has parameters, so it will fallback to them if they are undefined when the function is called. Therefore the output is `4`, when the function run without arguments as `fun()` the output is `6`.

### Question 30: How many hashes (#) will the following snippet send to the console?

```
lst = [[x for x in range(3)] for y in range(3)]
 
for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")
```

A. six
B. zero
C. nine
**D. three**

I guessed correctly, I assume that this was the list `lst = [[0,1,2], [0,1,2], [0,1,2]]` and the nested for loops merely check against those 6 values to see which are odd (not divisible by 2), so the answer is `1,1,1`.

### Question 31: What is the output of the following code if the user enters a 0?

```
try:
    value = input("Enter a value: ")
    print(int(value)/len(value))
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except TypeError:
    print("Very very bad input...")
except:
    print("Booo!")
```

A. 1.0
**B. 0.0**
C. Very very bad input...
D. Bad input...
E. Very bad input...
F. Booo!

Yeah, I do not get that `0.0` output at all. `input()` captures a user input and stores it as a string regardless of the user's input, then `len(value)` which is `1` in this case, so `0/1 = 0.0`. If an `int(input())` was used it would throw an error.

### Question 32: What is the expected behavior of the following program?

```
try:
    print(5/0)
    break
except:
    print("Sorry, something went wrong...")
except (ValueError, ZeroDivisionError):
    print("Too bad...")
```

A. The program will cause a `ZeroDivisionError` exception and output the following message: `Too bad...`
B. The program will cause a `ValueError` exception and output a default error message.
C. The program will cause a `ZeroDivisionError` exception and output a default error message.
D. The program will cause a `SyntaxError` exception.
E. The program will cause a `ValueError` exception and output the following message: `Too bad...`
**F. The program will raise an exception handled by the first `except` block.**

Another confusing PCEP question! The source code here is really bad and throws up 2 errors, the first of which is that `break` is not allowed in an `except` block, but also the exception hierarchy doesn't allow specific errors after a catch-all `except`.

### Question 33: What is the expected behavior of the following program?

```
foo = (1, 2, 3)
foo.index(0)
```

A. The program will cause a *ValueError* exception.
B. The program will cause an *AttributeError* exception.
C. The program will output `1` to the screen.
D. The program will cause a *TypeError* exception.
E. The program will cause a *SyntaxError* exception.

### Question 34: Which of the following snippets shows the correct way of handling multiple exceptions in a single except clause?

```
# A:
except (TypeError, ValueError, ZeroDivisionError):
    # Some code.
 
# B:
except TypeError, ValueError, ZeroDivisionError:
    # Some code.
 
# C:
except: (TypeError, ValueError, ZeroDivisionError)
    # Some code.
 
# D:
except: TypeError, ValueError, ZeroDivisionError
    # Some code.
 
# E:
except (TypeError, ValueError, ZeroDivisionError)
    # Some code.
 
# F:
except TypeError, ValueError, ZeroDivisionError
    # Some code.
```

F only
A and B
A and F
B and C
D and E
A only
A, C, and D

### Question 35: What will happen when you attempt to run the following code?

```
print(Hello, World!)
```

A. The code will print `Hello, World!` to the console.
B. The code will raise the *SyntaxError* exception.
C. The code will raise the *TypeError* exception.
D. The code will raise the *ValueError* exception.
E. The code will raise the *AttributeError* exception.