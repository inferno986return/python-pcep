# Collatz conjecture - a simplistic yet unsolved mathematical problem

# The steps for Collatz conjecture are as follows, as per Wikipedia:

# 1. Take a positive integer which is greater than or equal to 1 and label it as c0.
# 2. For even numbers, divide c0 by 2;
# 3. For odd numbers, multiply c0 by 3 and add 1.
# 4. With enough repetition, do all positive integers converge to 1?

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