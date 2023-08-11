#!/usr/bin/python3
import sys
import hidden_4
if __name__ == "__main__":
    lexis = dir(hidden_4)
    for lexi in lexis:
        if lexis[:2] != "__":
            print(lexi)
