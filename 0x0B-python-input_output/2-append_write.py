#!/usr/bin/python3
"""append write"""

def append_write(filename="", text=""):
    """appends a utf-8 encoded textfile
    """
    with open(filename, 'a', encoding='utf-8') as lines:
        return lines.write(text)
