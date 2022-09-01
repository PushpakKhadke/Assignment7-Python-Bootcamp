"""
8. Write a python script to check whether two given strings are identical, first string
comes before the second in dictionary order or first string comes after the second
string in dictionary order using match case statement
 """

string1=input("Enter First String: ")
string2=input("Enter Second String: ")
match (string1,string2):
    case (string1,string2) if string1==string2:
        print("Identical String")
    case (string1, string2) if string1>string2:
        print("{} comes after {}".format(string1,string2))
print()
