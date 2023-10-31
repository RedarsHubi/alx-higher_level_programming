#!/usr/bin/python3
"""

Module for class prevents the user from dynamically
creating new instance attributes, except for 1 case

"""


class LockedClass:
    __slots__ = ['first_name']

    def __init__(self):
        """ Init method """
        pass
