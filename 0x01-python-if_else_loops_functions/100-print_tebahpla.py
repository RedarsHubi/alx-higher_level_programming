#!/usr/bin/python3
result = ""
for i in range(123, 96, -1):
    if i%2 == 0:
        result += chr(i)
    else:
        result += (chr((i - 32)))
print("{}".format(result), end="")    
