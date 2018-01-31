# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 23:23:58 2018

@author: Wu Jingwei
"""

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (3**round((math.log(n,3))))==n if n>0 else False

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n>=3:
            n/=3.0
        if n==1:
            return True
        return False