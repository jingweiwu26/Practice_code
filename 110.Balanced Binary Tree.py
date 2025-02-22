# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 22:42:12 2017

@author: Wu Jingwei
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if abs(self.height(root.left)-self.height(root.right))<=1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
    
    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right))+1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def post_order(n: Optional[TreeNode]) -> int:
            if not n: return 0

            l = post_order(n.left)
            r = post_order(n.right)

            if abs(l-r) > 1: return -1
            if l == -1 or r == -1: return -1

            return max(l, r) +1
        
        res = post_order(root)
        return res != -1
