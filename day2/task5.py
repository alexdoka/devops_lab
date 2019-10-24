#!/usr/bin/env python
n = input("Enter numbers for n array: ")
a = input("Enter numbers for a-set: ")
b = input("Enter numbers for b-set: ")
n_array = n.split()
a_set = set(a.split())
b_set = set(b.split())
# n_array=[1, 5, 3, 5, 1]
# a_set={3, 1}
# b_set={5, 7}
happiness = 0
for number in n_array:
    if number in a_set:
        happiness += 1
    elif number in b_set:
        happiness -= 1
print(happiness)
