# -*- coding: utf-8 -*-
"""
Created on Mon Jan 08 22:40:45 2018

@author: Wu Jingwei
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        money = [0] * len(nums)
        money[0] = nums[0]
        money[1] = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            money[i] = max(money[i-2]+nums[i], money[i-1])
        return money[-1]