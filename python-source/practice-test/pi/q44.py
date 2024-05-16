my_list = [[c for c in range(r)] for r in range(3)]

for element in my_list:
    if len(element) < 2:
        print()