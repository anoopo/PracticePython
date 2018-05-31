"""Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year
 that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
(Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)"""
from datetime import datetime
import calendar

today = datetime.now()
this_year = today.year
this_month = today.month
#Get the user inputs
name = input("Enter your name : ")
age = int(input("Enter you age :"))
month_name = input("Enter your birth month:")
month = calendar.month_name(month_name)
if month > this_month:
    #Birthday has already been over
    century_year = (this_year - 1) + (100 - age)
else:
    century_year = this_year + (100 - age)
msg = "Hi {}, You will be 100 years old in {}".format(name,century_year)
print (msg)
print()
number = int(input("Enter a number:"))
print (("{}\n".format(msg))*number)
