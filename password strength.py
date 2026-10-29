import re

password = input("Enter your password: ")
score = 0

if len(password) >= 8: score += 1
if re.search(r"[A-Z]", password): score += 1
if re.search(r"[a-z]", password): score += 1
if re.search(r"[0-9]", password): score += 1
if re.search(r"[^A-Za-z0-9]", password): score += 1

print("\nPassword Strength:")
print("Weak" if score <= 2 else "Moderate" if score <= 4 else "Strong")