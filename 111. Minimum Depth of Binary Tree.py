# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 21:38:55 2017

@author: Wu Jingwei
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        level = 0
        current = [root]
        while current:
            level+=1
            next = []
            for root in current:
                if not root.left and not root.right:
                    return level
                if root.left:
                    next.append(root.left)
                if root.right:
                    next.append(root.right)
            current = next