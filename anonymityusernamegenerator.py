import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyUserNameAnonymity Generator!")
nr_letters= int(input("How many letters would you like in your UserName?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
for l_r in range(nr_letters):
    letters_r = random.choice(letters)
    password.append(letters_r)

for s_r in range(nr_symbols):
    symbols_r = random.choice(symbols)
    password.append(symbols_r)

for n_r in range(nr_numbers):
    numbers_r = random.choice(numbers)
    password.append(numbers_r)


random.shuffle(password)


result = ''.join(password)

# resulttoal
print(f"Your UserName is {result}")