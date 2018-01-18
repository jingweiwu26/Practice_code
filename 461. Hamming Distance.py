# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 22:36:08 2018

@author: Wu Jingwei
"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bin_x = list(("{:b}".format(x)))
        bin_y = list(("{:b}".format(y)))
        len_diff = len(bin_x)-len(bin_y)
        count=0
        if len_diff > 0:
            bin_y=['0']*len_diff + bin_y
        if len_diff < 0:
            bin_x=['0']*abs(len_diff) + bin_x
        for i, j in zip(bin_x,bin_y):
            count+= int(i)^int(j)    
        return count

class Solution(object):
    def hammingDistance(self, x, y):
        return bin(x^y).count('1')