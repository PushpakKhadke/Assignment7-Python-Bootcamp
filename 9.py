"""
 9. Write a python script to check whether a given year is
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. Century non leap year 
"""

year=int(input('Enter The Year: '))

match 'Century leap year' if year%400==0 else 'Century non leap year' if year%100==0 else 'Non century leap year' if year%4==0 else 'Non century non leap year':
    case 'Century leap year':
        print('It\'s Century Leap Year')
    case 'Century non leap year':
        print('It\'s Century Year, But Not a Leap Year')
    case 'Non century leap year':
        print('It\'s Not Century Year, But It\'s a Leap Year')
    case 'Non century non leap year':
        print('It\'s Not Century and Not Leap Year')
