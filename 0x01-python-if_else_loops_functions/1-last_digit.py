#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
temp = number
if (number < 0):
    temp = -1 * number
lastdigit = temp % 10
if (lastdigit > 5):
    text = "greater than 5"
elif (lastdigit == 0):
    text = "0"
elif ((lastdigit < 6) and (lastdigit != 0)):
    text = "less than 6 and not 0"

print("The Last digit of {} is {} and is {}".format(number,lastdigit,text))
