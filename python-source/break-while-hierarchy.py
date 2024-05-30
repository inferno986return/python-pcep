while True:
    print("outer loop")
    escape = input()
    if escape == "escape":
        break
    while escape == "":
        print("inner loop")

        