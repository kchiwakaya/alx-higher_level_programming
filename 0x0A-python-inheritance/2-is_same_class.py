#!/usr/bin/python3
"""class here"""

def is_same_class(obj, a_class):
    """returns True if the object is exactly an 
    instance of the specified class ; otherwise False
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class must be of type 'type'")
    return (type(obj) is a_class)
