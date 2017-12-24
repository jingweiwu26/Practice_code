# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 15:48:08 2017

@author: Wu Jingwei
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_idx=0
        right_idx=len(numbers)-1
        while left_idx<right_idx:
            if numbers[left_idx] + numbers[right_idx] == target:
                return left_idx+1, right_idx+1
            if numbers[left_idx] + numbers[right_idx] < target:
                left_idx+=1
            if numbers[left_idx] + numbers[right_idx] > target:
                right_idx-=1
            
        