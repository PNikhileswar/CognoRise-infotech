import random
import string

def generate_password(length):
    if length < 1:
        print("Password length must be at least 1")
    
    # Define possible characters
    all_chars = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# Get user input for password length
length = int(input("Enter the desired length of the password: "))
password = generate_password(length)
print(f"Generated password: {password}")

