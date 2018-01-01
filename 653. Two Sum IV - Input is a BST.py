# -*- coding: utf-8 -*-
"""
Created on Mon Jan 01 11:49:59 2018

@author: Wu Jingwei
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        collection=set()
        return self.helper(root, k, collection)       
    
    def helper(self, root,k,collection):
        if not root:
            return False
        if root.val in collection:
            return True
        collection.add(k-root.val)
        return self.helper(root.left,k,collection) or self.helper(root.right,k,collection)