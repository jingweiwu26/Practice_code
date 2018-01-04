# -*- coding: utf-8 -*-
"""
Created on Wed Jan 03 23:16:00 2018

@author: Wu Jingwei
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        max_nums=max(nums)
        node = TreeNode(max_nums)
        idx = nums.index(max_nums)
        l = nums[:idx]
        r = nums[idx+1:] if idx != len(nums)-1 else []
        node.left=self.constructMaximumBinaryTree(l)
        node.right = self.constructMaximumBinaryTree(r)
        return node 
            