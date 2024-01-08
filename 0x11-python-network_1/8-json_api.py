#!/usr/bin/python3
"""
posting data to web servers
"""
if __name__ == "__main__":
    import requests
    import sys
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    query = {'q': q}
    response = requests.post(url, data=query)
    if response.status_code != requests.codes.ok or len(response.text) <= 0:
        print('No result')
        sys.exit()
    else:
        try:
            myObject = response.json()
            if len(myObject) == 0:
                print('No result')
                sys.exit()
            theId = myObject.get('id')
            theName = myObject.get('name')
            print("[{}] {}".format(theId, theName))
        except ValueError as invalid_json:
            print('Not a valid JSON')
