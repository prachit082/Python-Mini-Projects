import random

# Prompt the user to enter the length of the password
passlen = int(input("Enter the length of the password: "))

# Define the character set for the password
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%^&*()?"

# Generate a random password of the specified length
p = "".join(random.sample(s, passlen))

# Print the generated password
print(p)
