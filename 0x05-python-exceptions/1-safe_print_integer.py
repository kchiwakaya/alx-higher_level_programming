#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        isInt = True
    except (ValueError, TypeError):
        isInt = False
    return isInt
