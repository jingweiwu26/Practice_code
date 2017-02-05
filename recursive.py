# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 15:12:49 2017

@author: Wu Jingwei
"""

arr=[1,2,[3,4,[5,6]]]

ar=[]

def unlist(arr_):
 # a list contain the unlist
    for i in arr_:
        if type(i)!= list:
            ar.append(i)
        else:
            for j in i:
                if type(j)!=list:
                    ar.append(j)
                else:
                    unlist(j)
    return ar
    
print unlist(arr)