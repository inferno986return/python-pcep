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

I ran this code snippet, but why is the answer A? I am convinced it was C.

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

Lists are unusual as when they are assigned to other variables like this they are merely referenced so `nums` and `vals` are the same list. This means that if `nums` changed in any way, `vals` would also be affected. Either a slice or method would need to be used to make nums a separate duplicate list.

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

This one is also very easy as it's a simple floor division operation so `1 // 2 = 0`. Floor division will *only output integers* or a DivideByZeroError in the case the divisor is zero `0`.

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

The order of positional arguments does matter, so the Python 3 interpreter won't allow this `print()` function and subsequently generates a SyntaxError.

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

`for` and `in` are reserved keywords in Python 3, using them as variables will result in a `SyntaxError`. As for the other answers, Python 2 used to reserve `print` as a statement, though since becoming a built-in function this restriction was dropped. Also since Python 3 is case-sensititive `In` is technically allowed. I wouldn't recommend either though as it may add unneccessary complexity to your source code.

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

Be careful with those nested list indicies for the `del` statement as it goes to the 2nd element of the list `4` and then uses that index to delete the 4th element `16`.

### Question 11:What is the output of the following piece of code?

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

This is another piece of devious PCEP code. The important thing to remember is the `1 1 2` and the key is to follow the variable as they are assigned from right to left.

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

The answer is `0 1` but I didn't get that correct. I first mistook the caret `^` which means bitwise XOR for bitwise AND whch uses the ampersand `&`. Then I didn't consider the two bits which comprise the variables `a = 01, b = 00`