# -*- coding: utf-8 -*-
"""
Created on Sat Feb 04 10:33:27 2017

@author: Wu Jingwei
"""

def now():
    print "2017-1-1"
    
f=now
f()

print f.__name__

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print "2017777"

now()