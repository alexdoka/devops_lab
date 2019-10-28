#!/usr/bin/env python
str = input("Input some sentense: ")
x = str.split()
for i in x: print(i[::-1], end=" ")