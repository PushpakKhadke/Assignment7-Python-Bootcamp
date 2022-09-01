"""
5. Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number.
"""

x = int(input("Enter The  Number: "))
print()
match x:
    case a:
        if x % 2 == 0:
            print("Saurabh Shukla")
            print()
        elif x < 0 and x % 2 != 0:
            print("Prateek Jain")
            print()
        elif x > 0 and x % 2 != 0:
            print("Aditya Choudhary")
            print()
