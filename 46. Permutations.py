# -*- coding: utf-8 -*-
"""
Created on Thu Feb 01 22:00:19 2018

@author: Wu Jingwei
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import permutations
        p=permutations(nums)
        return [list(i) for i in p]