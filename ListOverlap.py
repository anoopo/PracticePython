"""Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the
elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extras:

1.Randomly generate two lists to test this
2. Write this in one line of Python"""
import random
def listOverlap(list1,list2):
    return (list(set([x for x in list1 if x in list2])))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print (listOverlap(a,b))

print ("Extras")
a = random.sample(range(1,100),10)
b = random.sample(range(1,200),20)
print (a)
print (b)
print (listOverlap(a,b))
