#!/usr/bin/python3
""" Squre inherit rect"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ super class is BaseGeometry, then Rectangle
    """
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
