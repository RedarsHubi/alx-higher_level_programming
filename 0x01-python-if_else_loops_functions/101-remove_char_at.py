#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ""
    for i in range str:
        if i == n:
            copy += ""
        else:
            copy += i
    return copy
