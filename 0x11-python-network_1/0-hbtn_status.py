#!/usr/bin/python3
"""testing status of web pages
"""
if __name__ == "__main__":
    import urllib.request
    url = "https://intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        read_bytes = response.read()
        contents = read_bytes.decode('utf-8')
        print_string = '''Body response:
\t- type: {}
\t- content: {}
\t- utf8 content: {}'''.format(type(read_bytes), read_bytes, contents)
        print(print_string)
