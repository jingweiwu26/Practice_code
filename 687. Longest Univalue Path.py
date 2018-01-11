# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 22:41:59 2018

@author: Wu Jingwei
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.longestUnivaluePath(root.left), self.longestUnivaluePath(root.right), self.helper(root.val, root.left) + self.helper(root.val,root.right))
    
    def helper(self, p_val, c_root):
        if c_root and p_val==c_root.val:
            return 1 + max(self.helper(p_val, c_root.left), self.helper(p_val, c_root.right))
        return 0
