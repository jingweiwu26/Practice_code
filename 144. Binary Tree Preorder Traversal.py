# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 22:17:32 2018

@author: Wu Jingwei
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        self.push_res(res, root)
        return res
    def push_res(self, res, node):
        if not node:
            return res
        res.append(node.val)
        self.push_res(res, node.left)
        self.push_res(res, node.right)

class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []
        res= []
        stack = [root]
        while stack:
            current = stack.pop()
            res.append(current.val)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return res
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def traverse(n):
            if not n: return
            res.append(n.val)
            traverse(n.left)
            traverse(n.right)
        
        res =[]
        traverse(root)
        return res