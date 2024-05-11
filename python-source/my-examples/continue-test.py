#continue-test.py - demonstrate the continue keyword

for i in range(11):    
    if i % 2 != 0:
        continue

    print(i)
    i += 1