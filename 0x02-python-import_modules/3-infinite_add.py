#!/usr/bin/python3
import sys
if __name__ != '__main__':
    exit()
result = 0
for i in sys.argv[1:]:
    result = result + int(i)
print(result)
