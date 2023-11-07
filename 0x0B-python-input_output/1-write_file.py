#!/usr/bin/python3
"""Module for writing to a file"""


def write_file(filename="", text=""):
    """Writes to file and returns num of chars"""
    with open(file_path, 'w', encoding="utf-8") as f:
        data = f.write(text)
    return data
