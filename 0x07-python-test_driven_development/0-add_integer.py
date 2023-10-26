#!/usr/bin/python3
""" Module for functions that adds two numbers"""


def add_integer(a, b=98):
    """ Adds two ints

    Raises:
        TypeError: if a or b is not an int
    """
    if (type(a) == float) or (type(b) == float):
        a = int(a)
        b = int(b)
    if (type(a) == int) and (type(b) == int):
        return a + b
    if (type(a) != int) and (type(a) != float):
        raise TypeError("a must be an integer")
    elif (type(b) != int) and (type(b) != float):
        raise TypeError("b must be an integer")
