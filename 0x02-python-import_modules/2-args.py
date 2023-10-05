#!/usr/bin/python3
import sys
if __name__ != '__main__':
    sys.exit()

zab = len(sys.argv) - 1
index = 1
if zab == 1:
    print("{} argument:".format(zab))
elif zab == 0:
    print("{} arguments.".format(zab))
else:
    print("{} arguments:".format(zab))
    
for i in sys.argv[1:]:
    print("{}: {}".format(index, i))
        
    index = index + 1
