# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 12:35:34 2017

@author: Wu Jingwei
"""
class memo(object):
    def __init__(self,fn):
        self.fn=fn
        self.cache={}
    
    def __call__(self, args):
        if args not in self.cache:
            self.cache[args]=self.fn(args)
        return self.cache[args]

@memo
def fib(n):
    if n in [0,1]:
        return 1
    else:
        return fib(n-1) + fib(n-2)
"""
def memorize(fn, arg):
    memo={}
    if arg not in memo:
        memo[arg]=fn(arg)
    return memo[arg]
"""

for i in range(10):
    print fib(i)