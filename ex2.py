#!usr/bin/python3
import sys


def isWhiteLine(x):
    return x.isspace()


file_name = sys.argv[1]
f = open(file_name, "r")
for i in f:
    if (isWhiteLine(i) == False):
        print(str(i).strip())
f.close()
