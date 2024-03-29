# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 21:12:45 2018

@author: Wu Jingwei
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        root.left, root.right = root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        node = root
        node.left, node.right = self.invertTree(node.right), self.invertTree(node.left)
        return node
