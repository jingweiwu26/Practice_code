# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 10:11:13 2017

@author: Wu Jingwei
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        return self.root_finder(nums, 0, len(nums)-1)
    def root_finder(self, nums, start, end):
        if start > end:
            return None
        mid=(start+end)/2
        root=TreeNode(nums[mid])
        root.left=self.root_finder(nums, start, mid-1)
        root.right=self.root_finder(nums, mid+1, end)
        return root