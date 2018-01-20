# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 13:27:39 2018

@author: Wu Jingwei
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')