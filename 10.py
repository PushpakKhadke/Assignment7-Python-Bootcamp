"""
10. Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday

"""

ask=input("Enter Your Favorite Color: ")

match 'red' if 'red' in ask.lower() else 'yellow' if 'yellow' in ask.lower() else 'blue' if 'blue' in ask.lower() else 'orange' if 'orange' in ask.lower() else 'white' if 'white' in ask.lower() else 'black' if 'black' in ask.lower() else 'sunday':
    case 'yellow':
        print('Monday')
    case 'blue':
        print('Tuesday')
    case 'orange':
        print('Wednesday')
    case 'white':
        print('Thursday')
    case 'black':
        print('Friday')
    case 'red':
        print('Saturday')
    case 'sunday':
        print('Sunday')
