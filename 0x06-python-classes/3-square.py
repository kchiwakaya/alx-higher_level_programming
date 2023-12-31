#!/usr/bin/python3
"""Define class square"""


class Square:
    """
    Square class with attributes:
        size
    """
    def __init__(self, size=0):
        """
        constructor to check error input
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        calculate area
        """
        return self.__size ** 2
