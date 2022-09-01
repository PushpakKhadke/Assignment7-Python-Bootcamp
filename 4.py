"""
4. Write a program which takes user’s age and display the category of person. Age
below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
Experienced, Age above or equal 60 - Senior Citizen.
"""

Age= int(input("Enter Your Age: "))
match Age:
    case A:
        if Age < 10:
            print("You\'re a Kid")
        elif Age < 20:
            print("You\'re a Teen")
        elif Age < 40:
            print("You\'re a Young")
        elif Age < 60:
            print("You\'re a Experienced")
        elif Age > 60 or Age == 60:
            print("You\'re a senior Citizen")
