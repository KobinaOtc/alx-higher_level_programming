#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = 0
if number < 0:
    number *= -1
    num = 1
lastdig = number % 10
if num == 1:
    number *= -1
    lastdig *= -1
print("Last digit of {:d} is ".format(number), end="")
if lastdig > 5:
    print("{:d} and is greater than 5".format(lastdig))
elif lastdig == 0:
    print("{:d} and is 0".format(lastdig))
else:
    print("{:d} and is less than 6 and not 0".format(lastdig))
