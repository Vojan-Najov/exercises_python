#!/usr/bin/env python3

import time
from random import randrange

def findMinQuadratic(alist):
    "O(n) = n^2"

    overallmin = alist[0]
    for i in alist:
        issmallest = True
        for j in alist:
            if i > j:
                issmallest = False
        if issmallest:
            overallmin = i
    return overallmin

def findMinLinear(alist):
    "O(n) = n"

    minsofar = alist[0]
    for i in alist:
        if i < minsofar:
            minsofar = i
    return minsofar



# findMin = findMinQuadratic
# print(findMin([5, 4, 2, 1, 0]))
# print(findMin([0, 4, 2, 1, 5]))

def test(findMin):
    for listSize in range(1000, 10001, 1000):
        alist = [randrange(100000) for x in range(listSize)]
        start = time.time()
        print(findMin(alist))
        end = time.time()
        print(f"size: {listSize} time: {end - start}")

def main():
    print("---> Testing the Quadratic FindMin:")
    test(findMinQuadratic)
    print("---> Testing the Linear FindMin:")
    test(findMinLinear)

main()
