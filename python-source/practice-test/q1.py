my_list = [1, 2]

# my_list.insert(-1, 0) #insert() places the element before the index
# print(my_list) # outputs [1, 0, 2]
 
for v in range(2):
    my_list.insert(-1, my_list[v])
 
print(my_list)