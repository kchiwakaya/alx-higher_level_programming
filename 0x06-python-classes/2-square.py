#!/usr/bin/python3
"""Define class square"""
class Square:
    """
    square class with attributes:
        size
    """
    def __init__(self, size=0):
        """
        constructor which checks for
        for input errors for size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
