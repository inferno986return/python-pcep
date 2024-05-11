# lab19-vowel-eater.py
# BSD licenced

# Prompt the user to enter a word and assign it to the user_word variable.
user_word = input("Enter a word:")

# Convert input to uppercase
user_word = user_word.upper() 

# Define vowels to be eaten as a list which is more elegant than using elif statements
vowels = ["A","E","I","O","U"]
 
for letter in user_word:
    if letter in vowels:
        continue
    elif letter not in vowels:
        print(letter)
 