#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    prints the reverse of a list
    """
    num = len(my_list) -1
    while (num  != -1):
        print ("{}".format(my_list[num]))
        num -= 1
