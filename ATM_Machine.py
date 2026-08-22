# ATM Machine Project

correct_pin = 1234
balance = 5000

pin = int(input("Enter ATM PIN: "))

if pin == correct_pin:
    print("Login Successful")
    print("Your Balance is:", balance)
else:
    print("Access Denied")