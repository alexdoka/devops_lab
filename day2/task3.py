#!/usr/bin/env python


# string data in list convert to int
def str2int(mylist):
    for r in range(0, len(mylist)):
        mylist[r] = int(mylist[r])


# input squares's coordinates
sq = []
squares = int(input("Input number of squares "))
for l in range(squares):
    coord = input("Input coordinates of squares x1 y1 x2 y2 like 1 1 3 3:  ").split()
    str2int(coord)
    sq.append(coord)

holst = (input("Input width and hight of canvas (like 5 6): ")).split()
str2int(holst)
S_holst = holst[0] * holst[1]
s_squares = []
for c in range(squares):
    x1 = sq[c][0]
    y1 = sq[c][1]
    x2 = sq[c][2]
    y2 = sq[c][3]
    for i in range(x1, x2):
        for j in range(y1, y2):
            if [i + 1, j + 1] not in s_squares:
                s_squares.append([i + 1, j + 1])
print('Free part is {0}'.format(S_holst - len(s_squares)))
