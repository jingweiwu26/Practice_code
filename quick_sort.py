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
    

def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]
    return arr

def select_sort(arr):
    for i in range(len(arr)-1):
        max_idx=0
        for j in range(len(arr)-1-i):
            if arr[j+1]>arr[max_idx]:
                max_idx=j+1
        arr[max_idx],arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[max_idx]
    return arr

def count_sort(arr):
    res=[]
    max_val=max(arr)
    count=[0] * (max_val+1)
    for i in arr:
        count[i]+=1

    for j in range(len(count)):
            for k in range(count[j]):
                res.append(j)
    return res


