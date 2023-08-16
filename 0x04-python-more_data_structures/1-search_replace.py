#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda letter:letter if letter != search else replace,my_list))
