import random

# Define the character pools
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbol = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', 
          '^', '_', '`', '{', '|', '}', '~']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Welcome message
print("Welcome to the Random Password Generator!")

# Input from the user
n_letter = int(input("Number of letters you want: "))
n_symbol = int(input("Number of symbols you want: "))
n_numbers = int(input("Number of numbers you want: "))

# Generate the password
password = []

# Add random letters
for _ in range(n_letter):
    password.append(random.choice(letter))

# Add random symbols
for _ in range(n_symbol):
    password.append(random.choice(symbol))

# Add random numbers
for _ in range(n_numbers):
    password.append(random.choice(numbers))

# Shuffle the characters for randomness
random.shuffle(password)

# Convert the list to a string and print the result
print("Your generated password is:")
print(''.join(password))
