# -*- coding: utf-8 -*-
"""
Created on Sun Jan 07 13:15:31 2018

@author: Wu Jingwei
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        current_max=0
        res=nums[0]
        for i in nums:
            if i > current_max+i:
                current_max = i
            else:
                current_max += i
            res=max(current_max, res)
            print current_max, res
        return res

class Solution:
    def maxSubArray(self, nums: List[int]) -> int: # Greedy
        if max(nums)<0:
            return max(nums)
        curr_sum = 0
        max_sum = 0
        for num in nums:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(curr_sum, max_sum)
            print(num, curr_sum,max_sum)
        return max_sum
