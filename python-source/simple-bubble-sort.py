
def bubblesort(list):
    for i in range(len(list) - 1):
        swapped = False
        for j in range(len(list) - i - 1):
            if list[i] > list[i + 1]:
              swapped = True
              list[i + 1], list[i] = list[i], list[i + 1] 
            else:
                swapped = False
                return list
    return list
    

list = [8, 10, 6, 2, 4]
print(bubblesort(list))