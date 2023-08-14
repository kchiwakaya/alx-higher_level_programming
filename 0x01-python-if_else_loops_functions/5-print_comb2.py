#!/usr/bin/python3
text = ", "

for i in range(100):
    if i == 99:
        text = ""
    print("{:02d}".format(i), end=text)
print('')
