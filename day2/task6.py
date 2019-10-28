#!/usr/bin/env python
str = input("Input some sentense: ")
x = str.split()
# ./day2/task6.py:4:11: E701 multiple statements on one line (colon) if i do:
# for i in x: print(i[::-1], end=" ") so in 2 lines:
for i in x:
    print(i[::-1], end=" ")
