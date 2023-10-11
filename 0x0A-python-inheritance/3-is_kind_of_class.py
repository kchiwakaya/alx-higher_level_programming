#!/usr/bin/python3
"""he does"""

def is_kind_of_class(obj, a_class):
    """lass MyList that inherits from list
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class type must be 'type'")
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False
