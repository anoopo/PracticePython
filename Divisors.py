"""Create a program that asks the user for a number and then prints
   out a list of all the divisors of that number.
   (If you don’t know what a divisor is, it is a number that divides
   evenly into another number. For example, 13 is a divisor of 26
   because 26 / 13 has no remainder.)"""
import time
startTime = time.time()
userInput = int(input("Enter your number :"))
divisorList = [x for x in range(2,((userInput//2)+1)) if userInput % x == 0]
divisorList.append(userInput)
divisors = ",".join(str(i) for i in divisorList)
print ()
print ("Divisors of {0:d} are :".format(userInput))
print (divisors)
print ("Time = {} ".format(str(time.time()-startTime)))
