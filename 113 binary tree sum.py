# -*- coding: utf-8 -*-
"""
Created on Tue Sep 05 23:51:07 2017

@author: Wu Jingwei
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if root.val==sum and not root.left and not root.right:
            return True
        else:
            sub_sum=sum-root.val            
            return self.hasPathSum(root.left, sub_sum) or self.hasPathSum(root.right, sub_sum)