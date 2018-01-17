# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 21:40:58 2018

@author: Wu Jingwei
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for idx, i in enumerate(nums):
            if target-i in dic:
                return [idx, dic[target-i]]
            dic[i]=idx
        return None