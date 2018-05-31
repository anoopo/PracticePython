"""Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)"""
def checkPaliandrome(str):
    return str == str[::-1]

userString = str(input("Enter the string to be checked : "))
if checkPaliandrome(userString):
    print ("This is a paliandrome")
else:
    print ("This is not paliandrome")
