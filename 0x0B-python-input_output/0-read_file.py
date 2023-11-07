#!/usr/bin/python3
"""Module for reading text file"""


def read_file(filename=""):
    """Reads and prints"""
    with open(filename, 'r') as f:
        data = f.read()
    print(data)
