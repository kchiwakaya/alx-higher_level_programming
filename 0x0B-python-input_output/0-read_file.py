#!/usr/bin/python3
"""Read a file"""

def read_file(filename=""):
    """reads a textfile and print output
    """
    with open(filename, encoding='utf-8') as lines:
        print(lines.read(), end='')
