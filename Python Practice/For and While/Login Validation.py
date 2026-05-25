## A program to validate user login credentials, ensuring the username is at least 5 characters long and the password is at least 8 characters long.

while True:

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if len(username) < 5:
        print("Username must be at least 5 characters long.")
        continue

    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        continue


    print("Login successful!")
    break