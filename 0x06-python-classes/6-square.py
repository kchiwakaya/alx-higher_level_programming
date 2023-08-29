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
    @property
    def position(self):
        """
        getter for position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter for position
        """
        if not isinstance(value, type((0, 0))):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        calculate area of square
        """
        return self.__size ** 2
    def my_print(self):
        """
        prints the square using '#' 
        taking into account position (x, y) offsets
        """
    
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        i = 0
        for i in range(self.__size):
            j = 0
            x_pad = 0
            for x_pad in range(self.__position[0]):
                print(" ", end='')
            for j in range(self.__size):
                print("#", end='')
            print()
