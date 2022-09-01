# 7. Write a python program to check whether a given number is positive, negative or
# zero using match case statement

Number=int(input('Enter The Number: '))
match 'Positive' if Number>0 else 'Negative' if Number<0 else 'Zero':
    case 'Positive':
        print()
        print('It\'s Positive Number')
        print()
    case 'Negative':
        print()
        print('It\'s Negative Number')
        print()
    case 'Zero':
        print()
        print('It\'s Zero')
        print()
