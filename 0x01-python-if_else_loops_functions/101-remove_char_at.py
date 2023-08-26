#!/usr/bin/python3
def remove_char_at(str, n):
    theString = ""
    a = 0
 
    for character in str:
        if a != n:
            theString += character
        a += 1
    return (theString)

