#!/usr/bin/python3


def text_indentation(text):
    """
    prints a string of text with 2 new lines
    unit tests are provided
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    string = ""
    specials = ['.', '?', ':']
    for ch in text:
        string += ch
        if ch in specials:
            string += "\n\n"
    print(string, end='')
