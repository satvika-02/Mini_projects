# Login System

correct_username = "admin"
correct_password = "1234"

username = input("Enter Username: ")

if username == correct_username:
    password = input("Enter Password: ")

    if password == correct_password:
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Wrong Username")