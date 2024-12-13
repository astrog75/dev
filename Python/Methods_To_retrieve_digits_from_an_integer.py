# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 09:33:30 2022

@author: moty_
"""

from time import perf_counter

# Methods to retrieve digits of an integer n
#
#
# Method 1
t1_start = perf_counter()
def method1(n):
    nStr = str(n)
    digits = [d for d in map(int, nStr)]
    return digits
t1_stop = perf_counter()
print(t1_stop-t1_start)

# Method 2
t1_start = perf_counter()
def method2(n):
    digits = []
    while n != 0:
        digits.insert(0, n % 10)
        n //= 10
    return digits
t1_stop = perf_counter()
print(t1_stop-t1_start)

print(method2(45752))