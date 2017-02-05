# -*- coding: utf-8 -*-
"""
Created on Thu Feb 02 15:10:28 2017

@author: Wu Jingwei
"""

def lazy_sum(*args):
    def sum():
        ax=0
        for i in args:
            ax+=i
        return ax
    return sum
    
f=lazy_sum(1,3,5,7,9)

print f()