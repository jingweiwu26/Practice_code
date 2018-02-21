# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 23:11:09 2018

@author: Wu Jingwei
"""

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        size = len(nums)
        con_count = 1
        max_length = 1
        for i in range(size-1):
            if nums[i+1] > nums[i]:
                con_count += 1
                max_length = max(max_length, con_count)
            else:
                con_count = 1
        return max_length