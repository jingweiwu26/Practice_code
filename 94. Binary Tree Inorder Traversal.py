we# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 22:54:43 2018

@author: Wu Jingwei
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        self.tra(res, root)
        return res

    def tra(self, res, node):
        if not node:
            return
        if node.left:
            self.tra(res, node.left)
        res.append(node.val)
        if node.right:
            self.tra(res, node.right)

class Solution(object):
    def __init__(self):
        self.s=set()
    def inorderTraversal(self, root):
        if not root:
            return []
        res=[]
        stack = [root]
        while stack:
            current = stack.pop()
            if current:
                if current in self.s:
                    res.append(current.val)
                else:
                    stack.append(current.right)
                    stack.append(current)
                    self.s.add(current)
                    stack.append(current.left)
        return res
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def tra(n):
            if not n:
                return
            tra(n.left)
            res.append(n.val)
            tra(n.right)
            
        tra(root)
        return res
        