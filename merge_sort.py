# -*- coding: utf-8 -*-
"""
Created on Sat Dec 09 21:41:10 2017

@author: Wu Jingwei
"""

def merge_sort(a_list):
    if len(a_list)<=1:
        return a_list
    mid = len(a_list)//2
    first = merge_sort(a_list[:mid])
    second = merge_sort(a_list[mid:])
    return merge(first, second)
    
def merge(a,b):
    c=[]
    while a and b:
        if a[0] > b[0]:
            c.append(b[0])
            b.pop(0)
        else:
            c.append(a[0])
            a.pop(0)
    if a:
        c+=a
    if b:
        c+=b
    return c

l=[77, 20,17,26,31,54,44,55]
print merge_sort(l)
    