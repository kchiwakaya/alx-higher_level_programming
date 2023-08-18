#!/usr/bin/python3
def print_last_digit(number):
    temp = 0
    if (number < 0):
        temp = -(number)
    else:
        temp = number
    print(temp % 10, end="")
    return temp % 10
