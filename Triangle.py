# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 15:22:16 2017

@author: Wu Jingwei
"""
"""arr=[1,2,[3,4,[5,6]]]

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
"""
def tri():
    L=[1]
    while True:
        yield L
        L.append(0)
        L=[L[i-1]+L[i] for i in range(len(L))]
        
n=0      
for i in tri():
    print(i)
    n=n+1
    if n==10:
        break
