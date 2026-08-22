# Student Result System

name = input("Enter Student Name: ")
marks = int(input("Enter Marks: "))
attendance = int(input("Enter Attendance Percentage: "))

print("\nStudent Name:", name)

if marks >= 35:
    if attendance >= 75:
        print("Result: Pass")
    else:
        print("Result: Attendance Shortage")
else:
    print("Result: Fail")