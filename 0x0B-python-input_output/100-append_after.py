#!/usr/bin/python3
""" append after"""

def append_after(filename="", search_string="", new_string=""):
    """appends after search string instances in file
    """
    with open(filename, 'r', encoding='utf-8') as theFile:
        lines = theFile.readlines()

    for i, line in enumerate(lines):
        if search_string in line:
            lines.insert(i + 1, new_string)
    with open(filename, 'w', encoding='utf-8') as theFile:
        content = "".join(lines)
        theFile.write(content)
