#!/usr/bin/python3
def no_c(my_string):
    """Removes cC from string"""
    newstring =""
    for letter in my_string:
        if (letter not in {'c','C'}):
            newstring += letter
    return newstring
