# 2. Write a menu driven program to perform following operations - Addition, Subtraction, Multiplication, Division

First_Number = int(input("Enter First Number: "))
Second_Number = int(input("Enter Second Number: "))
print()
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Divsion")
print()
z = int(input("Enter Your Choice: "))
print()
match z:
    case 1:
        print(" Sum is",First_Number,"and",Second_Number,"is",":",First_Number + Second_Number)
        print()
    case 2:
        print(" Subtraction is", First_Number, "and", Second_Number, "is", ":", First_Number - Second_Number)
        print()
    case 3:
        print(" Multiplication is", First_Number, "and", Second_Number, "is", ":", First_Number * Second_Number)
        print()
    case 4:
        print(" Division is", First_Number, "and", Second_Number, "is", ":", First_Number / Second_Number)
        print()
    case _:
        print("Enter Valid Choice")
        print()
