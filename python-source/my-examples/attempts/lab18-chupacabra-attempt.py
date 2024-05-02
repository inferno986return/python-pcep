# lab18-chupacabra.py - an attempt at Lab 18 to create infinite loop until the secret phrase is inputted by the user
# 3-clause BSD License

#Technically this code works but it doesn't fulfill the Lab 18 criteria by using the break keyword

secret_word = "null" #initialision

while secret_word != "chupacabra":
    secret_word = input("Enter the secret word:")