#!/usr/bin/python3
""" Base Geometry class"""


class BaseGeometry():
    """to be inherited by shapes.
    """

    def area(self):
        """ method to calculate area of shape
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates integer input
        """
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")
