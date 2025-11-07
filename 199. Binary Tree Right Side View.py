# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 22:39:44 2018

@author: Wu Jingwei
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        current = [root]
        res=[]
        while current:
            next = []
            for node in current:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            res.append(node.val)
            current = next
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            temp = []
            res.append([n.val for n in queue][-1])
            for n in queue:
                if n.left:
                    temp.append(n.left)
                if n.right:
                    temp.append(n.right)
            queue = temp
        
        return res
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.res =[]
        self.depth=0
        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        self.traverse(root)
        return self.res
    
    
    def traverse(self, node):
        if not node: return
        
        self.depth+=1
        if len(self.res) < self.depth:
            self.res.append(node.val)
        
        self.traverse(node.right)
        self.traverse(node.left)
        self.depth -=1
        
        