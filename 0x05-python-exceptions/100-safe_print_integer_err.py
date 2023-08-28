#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        isInt = True
    except (ValueError,TypeError) as err:
        isInt = False
        sys.stderr.write("Exception: {}".format(err))
    return isInt
