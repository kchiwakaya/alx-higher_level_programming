#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ != "__main__":
    exit()

argc = len(argv) - 1
if argc != 3:
    print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
    exit(1)
elif argv[2] == '+':
    function = add
elif argv[2] == '-':
    function = sub
elif argv[2] == '*':
    function = mul
elif argv[2] == '/':
    function = div
else:
    print("Unknown operator. Available operators: +, -, *, and /")
    exit(1)

output = function(int(argv[1]), int(argv[3]))
print("{:d} {:s} {:d} = {:d}".format(int(argv[1]),
    argv[2], int(argv[3]), output))
