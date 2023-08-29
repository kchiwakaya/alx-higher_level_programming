#!/usr/bin/python3
"""Define class square"""


class Square:
    """
    square class with fields:
        size
    """
    def __init__(self, size=0):
        """
        constructor init size
        """
        if self.__validate_size(size):
            self.__size = size

    @property
    def size(self):
        """
        getter for size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter for size
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        calculate area of square
        """
        return self.__size ** 2
 
