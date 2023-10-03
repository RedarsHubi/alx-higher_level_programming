#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) < 123:
            print("{}".format(chr(ord(i)-32)), end="")
        elif ord(i) >= 65 and ord(i) < 91:
            print("{}".format(i))
