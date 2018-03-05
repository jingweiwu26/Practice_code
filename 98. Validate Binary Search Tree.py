# -*- coding: utf-8 -*-
"""
Created on Sun Mar 04 22:09:52 2018

@author: Wu Jingwei
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.node_validator(root, -sys.maxint,sys.maxint)
        
    def node_validator(self, node, min_val, max_val):
        if not node:
            return True
        if node.val <=min_val or node.val >=max_val:
            return False
        return self.node_validator(node.left, min_val, node.val) and self.node_validator(node.right, node.val, max_val)