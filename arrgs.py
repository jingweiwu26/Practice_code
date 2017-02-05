# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 20:24:00 2017

@author: Wu Jingwei
"""

def sq(*args):
    n=0
    for i in args:
       n+=i
    return n

print sq(1,2,3,4,5)

arr=[1,2,3,4,5]
print sq(*arr)


def ssq(**kw):
    for i in kw:
        print kw[i]
    
print ssq(city="abc")
