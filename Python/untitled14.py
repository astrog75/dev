# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:59:11 2022

@author: moty_
"""

def sumOfDigitsSquared(n):
    
    # Retrieve every digits
    sumOfDigitsSquared = 0
    
    while n > 0:
        n, digit = divmod(n, 10)
        sumOfDigitsSquared += pow(digit, 2)
    
    return sumOfDigitsSquared


def isHappy(n):

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sumOfDigitsSquared(n)
    
    return n == 1
        
print(isHappy(7))