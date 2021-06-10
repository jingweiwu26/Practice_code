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

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path, select):
            if not select:
                res.append(path[:])
                return
            for i in range(len(select)):
                path.append(select[i])
                backtrack(path, select[:i]+ select[i+1:])
                path.pop()
        backtrack([], nums)
        return res
    
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res
