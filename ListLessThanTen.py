"""Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list
that are less than 5.

Extras:

1. Instead of printing the elements one by one, make a new list that
    has all the elements less than 5 from this list in it and print out
    this new list.
2. Write this in one line of Python.
3. Ask the user for a number and return a list that contains only elements
   from the original list a that are smaller than that number given
   by the user."""

list1 = [1,2,3,4,5,6,7,8,9]
list2 = [9,99,5,55,2,22,5,66,1,3,5,1,43,6]
def printList(list):
    for i in list:
        if i < 5:
            print (i)

printList(list1)
print ("list2")
printList(list2)

print ("Extra#1 and #2")
print ([x for x in list1 if x<5])
print ("list2")
print ([x for x in list2 if x<5])

print ("Extra#3")
userInput = int(input("Enter a number :"))
print ([x for x in list1 if x<userInput])
print ("list2")
print ([x for x in list2 if x<userInput])
