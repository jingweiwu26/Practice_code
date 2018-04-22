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
        res = []
        self.traverse(root, res)
        size = len(res)
        l=0
        r=size-1
        while l<r:
            if res[l]+res[r]==k:
                return True
            if res[l]+res[r]>k:
                r-=1
            if res[l]+res[r]<k:
                l+=1
        return False

    def traverse(self, node, res):
        if not node:
            return
        if node.left:
            self.traverse(node.left, res)
        res.append(node.val)
        if node.right:
            self.traverse(node.right, res)
        return res
