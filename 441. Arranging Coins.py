# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 23:29:56 2017

@author: Wu Jingwei
"""

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return n
        l=1
        r=n
        while l<r:
            m=(l+r)/2
            if m+m*(m-1)/2>n:
                r=m
            else:
                l=m+1
        return l-1
 
        