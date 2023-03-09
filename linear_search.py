# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 10:11:20 2023

@author: tm0663
"""

"""
    This one takes an array A and a value v and returns i for which A[i]=v
"""

def linear_search(arr, v):
    k = 0
    for i in range(0, len(arr)):
        if arr[i] == v:
            k = i
            return k
        elif (i == (len(arr))-1) and arr[i] != v:
            return "NIL"
            