#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    prints the reverse of a list
    """
    if type(my_list) is list:
        newlist = my_list[0:]
        newlist.reverse()
        for i in range(len(newlist)):
            print("{}".format(newlist[i]))
