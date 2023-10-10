#!/usr/bin/python3
""" Studen class"""

class Student:
    """student class for use
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """representation of Student in json form
        """
        isstrings = True
        if isinstance(attrs, list):
            for ele in attrs:
                if not isinstance(ele, str):
                    isstrings = False
        else:
            isstrings = False

        return {key: value for (key, value) in self.__dict__.items()
                if key in list(self.__dict__.keys()) and
                (not isstrings or key in attrs)}

