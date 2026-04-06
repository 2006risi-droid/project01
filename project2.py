import random
import string

def show_title():
    print("===============================")
    print("      PASSWORD GENERATOR       ")
    print("===============================")

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(length):
        password += random.choice(chars)
    return password

show_title()
user_input = input("Enter password length: ")

if user_input.isdigit():
    length = int(user_input)
    if length > 0:
        result = generate_password(length)
        print("-------------------------------")
        print("Generated Password:", result)
        print("-------------------------------")
    else:
        print("Length must be greater than 0.")
else:
    print("Please enter a valid number.")