# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 13:54:15 2017

@author: Wu Jingwei
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size=len(nums)
        for i in range(size):
            for j in range(size-i-1):
                if nums[i]+nums[i+j+1]==target:
                    return [i, i+j+1]