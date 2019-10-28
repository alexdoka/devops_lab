#!/usr/bin/env python
N = int(input("Input number: "))
space = len(bin(N)[2:])
for i in range(1, N + 1):
    print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=space))
