#!/usr/bin/python3
""" Module for functions that adds two numbers"""


def add_integer(a, b=98):
    """ Adds two ints

    Raises:
        TypeError: if a or b is not an int or float
    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int (b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
