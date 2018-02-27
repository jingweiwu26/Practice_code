# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 21:30:17 2018

@author: Wu Jingwei
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        dic = defaultdict(int)
        for i in nums:
            dic[i]+=1
        for i in dic:
            if dic[i]==1:
                return i