# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 09:21:05 2018

@author: Wu Jingwei
"""

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res=[]
        for i in range(num+1):
            i = '{:b}'.format(i)
            res.append(i.count('1'))
        print res
        return res

class Solution(object):
    def countBits(self, num):
        dp = [0]
        while len(dp) <= num :
            dp += map(lambda x:x+1, dp)
            print dp
        return dp[:num+1]