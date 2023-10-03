#!/usr/bin/python3


def uppercase(str):
    result = ""
    index = 0
    for i in str:
        if ord(i) >= 97 and ord(i) < 123:
            result += (chr(ord(i)-32)) if index < len(str) - 1 else "\n"
        elif ord(i) >= 65 and ord(i) < 91:
            result += i
        elif i == " " or i == ",":
            resutl += i

        index = index + 1
    print(result)
