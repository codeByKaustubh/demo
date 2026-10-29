correct_password = "Cyber123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password: ")

    if password == correct_password:
        print("Login Successful")
        break
    else:
        attempts += 1
        print("Incorrect Password")

if attempts == max_attempts:
    print("Account Locked")