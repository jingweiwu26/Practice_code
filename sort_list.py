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

def bubble(array):
    for j in range(len(array)):
        fliptoright(array)
    return array


#########################################

def fliptoright2(array):
    maxposition=0
    maxnumber=array[0]
    for i in range(len(array)):
        if array[i]>maxnumber:
            maxposition=i
            maxnumber=array[i]
    temp=array[-1]
    array[-1]=maxnumber
    array[maxposition]=temp
    return array

def select(array):
    length = len(array)
    for j in range(len(array)):
        array[:(length-j)]=fliptoright2(array[:(length-j)])
    return array

def select2(array):
    for j in range(len(array)-1):
        maxposition=0
        maxnumber=array[0]
        for i in range(len(array)-j):
            if array[i]>maxnumber:
                maxposition=i
                maxnumber=array[i]
        temp=array[-1-j]
        array[-1-j]=maxnumber
        array[maxposition]=temp
    return array



import timeit
iterative= timeit.timeit(
"bubble([5,4,3,2,1])",
"""
def fliptoright(array):
    for i in range(len(array)-1):
        if array[i]>array[i+1]:
            temp = array[i]
            array[i]=array[i+1]
            array[i+1]=temp
    return array

def bubble(array):
    for j in range(len(array)):
        fliptoright(array)
    return array
""",
number=10000 ) # otherwise it takes 3 minutes

print( "Iterative", iterative )

        