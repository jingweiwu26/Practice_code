# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 22:17:14 2018

@author: Wu Jingwei
"""

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original=list(nums)
        self.nums=nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.original

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        import random
        random.shuffle(self.nums)
        return self.nums