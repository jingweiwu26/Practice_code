# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 22:24:02 2018

@author: Wu Jingwei
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        r=set()
        while n!=1:
            n=reduce(lambda x,y:x+y, map(lambda x:x*x, map(int,list(str(n)))))
            if n not in r:
                r.add(n)
            else:
                return False
        return True