# lab18-chupacabra.py - demonstration of using the break keyword to terminate an otherwise infinite loop

while True:
    secret_word = input("Enter the secret word:")

    if secret_word == "chupacabra":
        print("You've successfully left the loop.")
        break