# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 23:14:25 2017

@author: Wu Jingwei
"""

def quick_sort(arr):
    if len(arr) in (0,1): 
        return arr
    else:
        pivot = arr[0]
        i=0
        for j in range(len(arr)-1):
            if arr[j+1]<pivot:
                arr[j+1], arr[i+1]= arr[i+1], arr[j+1]
                i+=1
        arr[0], arr[i] = arr[i], arr[0]
        first_part = quick_sort(arr[:i])
        sec_part = quick_sort(arr[i+1:])
        first_part.append(arr[i])
        return first_part + sec_part
    
alist=[9,8,11,23,1,2,4]
print quick_sort(alist)    