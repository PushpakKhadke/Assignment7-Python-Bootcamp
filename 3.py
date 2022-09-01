"""
3. Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit.
"""

A=int(input("Enter 1st Number: "))
B=int(input("Enter 2nd Number: "))
C=int(input("Enter 3rd Number: "))
print()
print("1. Set of three numbers are lengths of an isosceles triangle or not")
print("2. Set of three numbers are lengths of sides of a right angled triangle or not")
print("3. Set of three numbers are equilateral triangle or not ")
print()

X = int(input("Enter your choice: "))
match X:
    case 1:
        if A == B or B == C or C == A:
            print("Length of an isosceles triangle")
        else:
            print("Not an isosceles triangle")
    case 2:
         T = A * A + B * B
         T1 = C * C
         if T == T1:
            print("Triangle is right angled triangle")
         else:
            print("Triangle is not right angled triangle")
    case 3:
        if A == B and C == A:
            print("Equilateral triangle")
        else:
            print("Not equilateral triangle")
