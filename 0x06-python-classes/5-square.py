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
        return (self.__size ** self.__size)

    def my_print(self):
        """
        prints the square using '#' characters
        """
        for i in range(self.__size):
            j = 0
            for j in range(self.__size):
                print("#", end='')
            print()
