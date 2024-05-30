try:
    print(5/0)
except (TypeError, ValueError, ZeroDivisionError):
    print("Oh no")
except:
    print("Oh yes")