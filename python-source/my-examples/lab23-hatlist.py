# lab23-hatlist.py - a magical hat with numbers instead of a cute rabbit.
# 3-clause BSD License

# There once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
 
# Step 2: write a line of code that removes the last element from the list.
 
# Step 3: write a line of code that prints the length of the existing list.

hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

hat_list[2] = int(input("Replace the middle number with another integer:"))
del hat_list[-1]
print(len(hat_list))
 
print(hat_list)