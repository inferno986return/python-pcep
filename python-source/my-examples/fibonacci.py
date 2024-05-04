# fibonacci.py - Output the full Fibonacci sequence up to a given integer with the formula: F(n) = F(n-1) + F(n-2)

def fibonacci(n=10):
    f = []
    x, y = 0, 1

    while x <= n:
        f.append(x)
        x, y = x, x + y

    return f

print(fibonacci(10))