#!/usr/bin/python3
"""Rect"""


class Rectangle():
    """rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"
    def __init__(self, width=0, height=0):
        """ 
        values for object creation
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ p__str__ method for object when str()
        / print() are invoked
        """
        _string = ""
        if self.width == 0 or self.height == 0:
            return _string

        for i in range(0, self.height):
            for j in range(0, self.width):
                _string += str(self.print_symbol)
            if i != self.height - 1:
                _string += '\n'
        return _string
    def __repr__(self):
        """ 
        provides __repr__ method for object when repr()
            is called, or eval().
        """
        _string = "Rectangle("
        _string += str(self.width)
        _string += ", " + str(self.height) + ")"
        return _string

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
    
    def __del__(self):
        """ called when a rectangle object is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
