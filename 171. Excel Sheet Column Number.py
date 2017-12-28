# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 22:13:40 2017

@author: Wu Jingwei
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return reduce(lambda x,y: 26*x+y, map(lambda x:ord(x)-64, s))
    
        