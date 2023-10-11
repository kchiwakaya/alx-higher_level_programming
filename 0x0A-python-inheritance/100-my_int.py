#!/usr/bin/python3
"""class again"""


class MyInt(int):
    """inversed int
    """

    def __eq__(self, other):
        return (int(self) != other)

    def __ne__(self, other):
        return (int(self) == other)
