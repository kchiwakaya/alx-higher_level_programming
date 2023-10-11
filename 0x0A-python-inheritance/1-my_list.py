#!/usr/bin/python3
"""Mylist class"""

class MyList(list):
    """version control
    """
    def print_sorted(self):
        """that prints the list, but sorted (ascending sort)
        """
        copy = self[:]
        copy.sort()
        print(copy)
