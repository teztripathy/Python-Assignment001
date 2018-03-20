#!/usr/bin/python3


def ruler():
    x = int(input("Give a number:  "))
    i = 1
    s1 = ""
    s2 = " "
    while (i <= x):
        s1 += str(i % 10)
        i += 1
        if (i % 10 == 0):
            s2 += str(int(i / 10))
        else:
            s2 += " "
    print(s2)
    print(s1)


ruler()
