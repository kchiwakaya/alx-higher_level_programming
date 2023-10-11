#!/usr/bin/python3
"""square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square shape class, super class is BaseGeometry
    """
    def __init__(self, size):
        """instantiation class
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """str method for class
        """
        string = "[Square] " + str(self.__size) + '/'
        string += str(self.__size)
        return string
