"""Ask the user for a number. Depending on whether the number is even or odd,
   print out an appropriate message to the user. Hint: how does an even / odd number react differently
   when divided by 2?

Extras:
1. If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
   If check divides evenly into num, tell that to the user. If not, print a different appropriate message."""

print ("First Exercise")
checkEven = int(input("Enter a number : "))
if checkEven % 2 == 0:
    print (f"{checkEven} is an even number")
else:
    print (f"{checkEven} is an odd number")

print ()
print ("Extra exercise # 1")
if checkEven > 3 and checkEven % 4 == 0:
    print (f"{checkEven} is a multiple of 4")
else:
    print (f"{checkEven} is not a multiple of 4")

print ()
print ("Extra exercise # 2")
num = int(input("Enter the number to check : "))
check = int(input("Enter the number to divide by : "))
if num >= check and num % check == 0:
    print (f"{num} is a multiple of {check}")
else:
    print (f"{num} is not a multiple of {check}")
