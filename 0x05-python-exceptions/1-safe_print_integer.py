#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except typo:
        None
    if value - 0 == value:
        return True
    else:
        return False
