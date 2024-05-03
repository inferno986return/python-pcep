# lab23-beatles.py

# step 1: create an empty list named beatles;
# step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
# step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
# step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
# step 5: use the insert() method to add Ringo Starr to the beginning of the list.

beatles = [] 
print("Step 1:", beatles)
 
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# stu = input("Add Stu Sutcliffe:")
# pete = input("Add Pete Best:")

# I struggle with this particular for loop
for members in range(1):
    beatles.append("Stu Sutcliffe")
    beatles.append("Pete Best")
print("Step 3:", beatles)

# Initially I used del beatles[4] which technically works, but isn't the most elegant
del beatles[-1]
del beatles[-1]
print("Step 4:", beatles)
 
beatles.insert(0,"Ringo Starr")
print("Step 5:", beatles)

# testing list length
print("The Fab", len(beatles))