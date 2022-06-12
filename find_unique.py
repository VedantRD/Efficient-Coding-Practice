# Given an array of integers, find and print the unique element.
# input  => 1,1,5,4,3,3,5,6,7,2,7,6,2
# output => 4

# ============================ Naive approach =================================

import functools


def findLonely(arr):
    d = {}
    if len(arr) == 1:
        return 1
    else:
        for n in arr:
            if n in d.keys():
                d[n] += 1
            else:
                d[n] = 1
        for n in d.keys():
            if d[n] == 1:
                return n


arr = [1, 1, 5, 4, 3, 3, 5, 6, 7, 2, 7, 6, 2]
# arr = []
print(findLonely(arr))
print(findLonely(arr))

# ========================= Efficient approach ================================


arr = [1, 1, 5, 4, 3, 3, 5, 6, 7, 2, 7, 6, 2]


def findLonelyEfficient(arr):
    return functools.reduce(lambda x, y: x ^ y, arr)

# print(findLonelyEfficient(arr))
