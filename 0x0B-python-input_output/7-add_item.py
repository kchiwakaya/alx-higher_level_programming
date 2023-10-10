#!/usr/bin/python3
"""taking arguments and adds to a list, saves to file
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """contain main code in function
    """
    try:
        _list = load_from_json_file('add_item.json')
    except:  
        _list = []

    _list.extend([sys.argv[i] for i in range(0, len(sys.argv)) if i != 0])
    try:
        save_to_json_file(_list, 'add_item.json')
    except:
        pass

main()
