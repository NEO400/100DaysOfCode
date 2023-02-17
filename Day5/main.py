# Password Generator Project
import random    # Import random library
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for character in range(1, nr_letters + 1):
    # Choose a random letter from the list of letter
    password += random.choice(letters)

for character in range(1, nr_symbols + 1):
    # Choose a random symbol from the list of symbols
    password += random.choice(symbols)

for character in range(1, nr_numbers + 1):
    # Choose a random number from the list of numbers
    password += random.choice(numbers)

print(password)    # Print the generated password

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []
for character in range(1, nr_letters + 1):
    # Choose a random letter from the list of letter
    password_list += random.choice(letters)

for character in range(1, nr_symbols + 1):
    # Choose a random symbol from the list of symbols
    password_list += random.choice(symbols)

for character in range(1, nr_numbers + 1):
    # Choose a random number from the list of numbers
    password_list += random.choice(numbers)

print(password_list)    # Print the list of password generated
random.shuffle(password_list)    # Shuffle the list of generated password
print(password_list)    # Print the shuffeled list of password

password = ""
for Character in password_list:
    # Concatenate each character of the list to form a string (password)
    password += Character
