# 1. Write a python script to display the number of days in a given month number.

x = eval(input("Enter Month Number: "))
match x:
    case 1:
        print("31 Days")
    case 2:
        print("28 or 29 Days")
    case 3:
        print("31 Days")
    case 4:
        print("30 Days")
    case 5:
        print("31 Days")
    case 6:
        print("30 Days")
    case 7:
        print("31 Days")
    case 8:
        print("31 Days")
    case 9:
        print("30 Days")
    case 10:
        print("31 Days")
    case 11:
        print("30 Days")
    case 12:
        print("31 Days")
    case _:
        print("Enter Valid Number")

