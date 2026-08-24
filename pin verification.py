pin = 1234
balance = 1000

user_pin = int(input("Enter ATM PIN: "))

if user_pin == pin:

    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Balance =", balance)

        elif choice == 2:
            amount = int(input("Enter deposit amount: "))
            balance += amount
            print("Deposit Successful")
            print("New Balance =", balance)

        elif choice == 3:
            amount = int(input("Enter withdrawal amount: "))

            if amount <= balance:
                balance -= amount
                print("Withdrawal Successful")
                print("New Balance =", balance)
            else:
                print("Insufficient Balance")

        elif choice == 4:
            print("Thank You for Using ATM")
            break

        else:
            print("Invalid Choice")

else:
    print("Incorrect PIN")