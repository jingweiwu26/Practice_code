# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 21:20:34 2018

@author: Wu Jingwei
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = reduce(lambda x,y: x^y, nums)
        mask = temp & (-temp)
        res = [0, 0]
        for i in nums:
            if i & mask:
                res[0]^=i
            else:
                res[1]^=i
        return res