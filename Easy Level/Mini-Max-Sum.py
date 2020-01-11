#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 6 10:59:49 2020

@author: suryakantkumar
"""

'''
Problem : Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

For example, arr = [1, 3, 5, 7, 9]. Our minimum sum is 1 + 3 + 5 + 7 = 16 and our maximum sum is 3 + 5 + 7 + 9 = 24. We would print

16 24
'''


def MiniMaxSum(li):    
    summ = 0
    
    for ele in li:
        summ += ele
            
    min_sum = summ - li[len(li) - 1]
    max_sum = summ - li[0]
    
    return min_sum, max_sum

li = [int(i) for i in input().strip().split()]
min_sum, max_sum = MiniMaxSum(li)
print(min_sum, max_sum)