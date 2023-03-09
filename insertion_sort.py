# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 11:56:38 2023

@author: tm0663
"""

import random
import numpy

A = [31,41,59,26,41,58]


def non_decreasing_insertion_sort(arr):
    """
        This function sorts the array in nondecreasing order.
        Thus, from the smallest to the largest
    """
    for j in range(1, len(arr)):
        key = arr[j]
        i = j-1
        while(i >= 0 and arr[i] > key):
            arr[i+1] = arr[i]
            print(f"A in while loop {i}: ", arr)
            i = i-1
            print("\n")
        arr[i+1] = key
        print(arr)
    

def non_increasing_insertion_sort(arr):
    """
        This function sorts the array in nonincreasing order.
        Thus, from the largest to the smallest
    """
    for j in range(1, len(arr)):
        key = arr[j]
        i = j-1
        while(i >= 0 and arr[i] < key):
            arr[i+1] = arr[i]
            print(f"A in while loop {i}: ", arr)
            i = i-1
            print("\n")
        arr[i+1] = key
        print(arr)
        
non_increasing_insertion_sort(A)
    