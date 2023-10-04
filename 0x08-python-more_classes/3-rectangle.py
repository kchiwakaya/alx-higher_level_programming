#!/usr/bin/python3
"""Rect"""


class Rectangle():
    """rectangle class
    """
    def __init__(self, width=0, height=0):
        """ 
        values for object creation
        """
        self.width = width
        self.height = height

    def __str__(self):
        """ p__str__ method for object when str()
        / print() are invoked
        """
        str = ""
        if self.width == 0 or self.height == 0:
            return str

        for i in range(0, self.height):
            for j in range(0, self.width):
                str += '#'
            if i != self.height - 1:
                str += '\n'
        return str

    @property
    def width(self):
        """ getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value


    @property
    def height(self):
        """ getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

   
    def area(self):
        """ public instance method to return area"""
        return (self.width * self.height)

    def perimeter(self):
        """ public instance method for the perimeter """
        if self.width == 0 or self.height == 0:
            return 0
        return ((2 * self.width) + (2 * self.height))

