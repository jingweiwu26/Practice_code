# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 23:13:49 2018

@author: Wu Jingwei
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        from collections import deque
        res=deque(nums)
        res.rotate(k)
        for i in range(len(nums)):
            nums[i]=res[i]
