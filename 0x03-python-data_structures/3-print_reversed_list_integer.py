#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    prints the reverse of a list
    """
    startindex = -1
    while (startindex != -len(my_list)- 1):
        print("{}".format(my_list[startindex]))
        startindex = startindex - 1
