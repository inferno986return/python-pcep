# break-test.py - let's test break

i = 0

while True:
    i += 1
    if i == 500:
        print(i, "- breaking the loop now")
        break