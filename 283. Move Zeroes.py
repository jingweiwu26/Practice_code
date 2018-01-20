# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 21:35:14 2018

@author: Wu Jingwei
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k=0
        for num in nums:
            if num:
                nums[k]=num
                k+=1
        nums[k:]=[0] * (len(nums)-k)
