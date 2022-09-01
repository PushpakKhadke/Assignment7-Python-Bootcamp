# 6. Write a python program to check whether a given string is a multiword string or single word string using match case statement

string=input("Enter The String: ")
string.strip()
match string:
    case string if ' ' in string:
        print("Multiword String!")
    case string if ' ' not in string:
        print("Singleword String!")
print()
