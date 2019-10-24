#!/usr/bin/env python
str = input("Input some sentense: ")
x = str.split()
i = 0
while i < len(x):
    print(x[i][::-1], end=" ")
    i += 1
