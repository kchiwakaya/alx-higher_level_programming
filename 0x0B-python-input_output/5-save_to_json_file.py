#!/usr/bin/python3
"""writing json strings to files
"""


import json


def save_to_json_file(my_obj, filename):
    """saves object to a file,
    overwriting previous contents
    """
    with open(filename, 'w', encoding='utf-8') as lines:
        return lines.write(json.dumps(my_obj))

