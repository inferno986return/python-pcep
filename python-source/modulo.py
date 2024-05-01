def modulo(x, y):
    z = x // y # Divide as usual, but force an integer
    m = z * y # Multiply the quotient by the divisor
    r = x - m # Subtract the dividend1 to find remainder
    return r

x = int(input("x: "))
y = int(input("y: "))
print("Remainder:", modulo(x, y))
print("Should be:", x % y)