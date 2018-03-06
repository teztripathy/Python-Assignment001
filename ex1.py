#!/usr/bin/python3

x = int(input("Give a number:  "))
i = 1
s1 = ""
while (i <= x):
    s1 += str(i % 10)
    i += 1
print(s1)
