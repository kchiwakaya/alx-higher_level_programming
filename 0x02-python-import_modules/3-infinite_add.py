#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    result = 0
    a = 1
    while a < len(sys.argv):
        result += int(sys.argv[a])
        a += 1
    print("{}".format(result))
