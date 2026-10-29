import secrets
import string

length = int(input("Enter password length: "))
characters = string.ascii_letters + string.digits + "!@#$%^&*"
password = ''.join(secrets.choice(characters) for _ in range(length))

print("Generated Password:", password)