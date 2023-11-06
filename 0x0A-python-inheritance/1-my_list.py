#!/usr/bin/python3
"""Module for available attributes and methods of an object"""


class MyList(list):
    """prints list in a sorted manner"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
