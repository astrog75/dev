# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 09:25:35 2023

@author: moty_
"""

def gcd(a, b):
    
    if a > b:
        while b > 0:
           a, b = b, a % b
        return a
    else:
        return gcd(b, a)
    

print(gcd(61
          , 15))