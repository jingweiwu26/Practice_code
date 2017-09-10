# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 15:04:28 2017

@author: Wu Jingwei
"""
class memo(object):
    def __init__(self, fn):
        self.fn=fn
        self.cache={}
    def __call__(self, *args):
        if self.fn(*args) not in self.cache:
            self.cache[args]=self.fn(*args)
        return self.cache[args]

@memo
def pow(x, n):
    if n==0:
        return 1
    if n==1:
        return x
    if n%2!=0:
        return pow(x, n-1)*x
    elif n%2==0:
        t=pow(x, n/2)
        return t*t

print pow(5,2)