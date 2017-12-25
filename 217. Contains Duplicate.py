# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 09:23:54 2017

@author: Wu Jingwei
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(set(nums)) == len(nums):
            return False
        return True