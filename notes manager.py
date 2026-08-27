while True:
    print("\n===== Notes Manager =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        note = input("Enter your note: ")

        file = open("notes.txt", "a")
        file.write(note + "\n")
        file.close()

        print("Note saved successfully!")

    elif choice == "2":
        try:
            file = open("notes.txt", "r")
            print("\n--- Your Notes ---")
            print(file.read())
            file.close()
        except FileNotFoundError:
            print("No notes found!")

    elif choice == "3":
        print("Thank you for using Notes Manager!")
        break

    else:
        print("Invalid choice!")