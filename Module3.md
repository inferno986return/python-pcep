# Python Essentials 1 - Module 3: 

## Section 2

### LAB: Collatz conjecture

Collatz conjecture is an unsolved yet simplistic mathematical problem and the second lab exercise for while loops. For the sake of this Python lab, every c0 which is a positive integer (that isn't zero) with enough steps can be made equal to 1.

1. Take a positive integer which is greater than or equal to 1 and label it as c0.
2. For even numbers, divide c0 by 2;
3. For odd numbers, multiply c0 by 3 and add 1.
4. With enough repetition, do all positive integers converge to 1?

The PCEP example for `c0 = 15` might be incorrect. Here's my output:

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

# Section 3

## Logical expressions

In electronics, there are logic gates. In the PCEP, you need to know these - AND, OR, NOT

>  Wiktionary defines **conjuction** as: (logic) The proposition resulting from the combination of two or more propositions using the `∧` operator.

AND is a conjunction, all inputs must be a `1` to get an output of `1`, as per the truth table below:

> Wiktionary defines **disjunction** as: (mathematics) A logical operator that results in “true” when some of its operands are true.

OR is a disjunction, it is flexible so if at least 1 input is a `1` then the output will be `1`

NOT simply flips the output from `0` to `1` and vice-versa. In electronic engineering, the NOT gate is called an *inverter* as it will invert the output.

Using NOT NOT results in a double negative effect similar to statements made in English such as: *"I will not not leave the house today"*. Also, using two minus signs together negates them into a plus `1 -- 1 = 2`

### Order of operations

Much like the mathematical operators from Section 2, logical operators are evaluated in a fixed order:

1. NOT
2. AND
3. OR



