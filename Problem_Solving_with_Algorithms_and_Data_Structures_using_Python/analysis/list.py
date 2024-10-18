#!/usr/bin/env python3

import timeit

def test1():
    l = []
    for i in range(1000):
        l += [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

def main():
    t1 = timeit.Timer("test1()", "from __main__ import test1")
    print(f"concat         {t1.timeit(number=1000):.6} milliseconds")
    t2 = timeit.Timer("test2()", "from __main__ import test2")
    print(f"append         {t2.timeit(number=1000):.6} milliseconds")
    t3 = timeit.Timer("test3()", "from __main__ import test3")
    print(f"comprehension  {t3.timeit(number=1000):.6} milliseconds")
    t4 = timeit.Timer("test4()", "from __main__ import test4")
    print(f"list range     {t4.timeit(number=1000):.6} milliseconds")


main()

x = list(range(2000000))
popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
print(f"popzero {popzero.timeit(number=1000):.8} milliseconds")

x = list(range(2000000))
popend = timeit.Timer("x.pop()", "from __main__ import x")
print(f"popend  {popend.timeit(number=1000):.8} milliseconds")

