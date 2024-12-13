# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 12:49:53 2023

@author: moty_
"""

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

def searchRange(nums, target):
    
    l = 0
    r = len(nums)-1
    while l <= r:
        middle = l + (r-l)//2
        if target < nums[middle]:
            r = middle - 1
        elif target > nums[middle]:
            l = middle + 1
        else:
            start = middle
            while start >=0 and nums[start] == target:
                start -= 1
            
            end = middle
            while end < len(nums) and nums[end] == target:
                end += 1
            
            return [start+1, end-1]
    
    return [-1, -1]

nums = [5,7,7,8,8,9,9,10,10,10,11,12,13]
target = 9
# expected : [5, 6]

print(searchRange(nums, target))