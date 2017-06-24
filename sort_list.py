# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 15:15:09 2017

@author: Wu Jingwei
"""

def fliptoright(array):
    for i in range(len(array)-1):
        if array[i]>array[i+1]:
            temp = array[i]
            array[i]=array[i+1]
            array[i+1]=temp
    return array

def select(array):
    length = len(array)
    for j in range(length):
        array[:(length-j)]=fliptoright(array[:(length-j)])
    return array

array=[5,4,3,2]

print select(array)