#!/usr/bin/env python
def invert(sent):
    x = sent.split()
    string = " ".join(i[::-1] for i in x)
    return string

if __name__ == "__main__":
    print(invert(input("Input some sentense: ")))