# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 13:25:55 2018

@author: Wu Jingwei
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        current = [s]
        while current:
            next=[]
            for i in current:
                if self.isSameNode(i, t):
                    return True
                next.append(i.left)
                next.append(i.right)
                next=filter(None, next)
            current=next
        return False

    def isSameNode(self, node_1, node_2):
        if not node_1 and not node_2:
            return True
        if node_1 and node_2 and node_1.val == node_2.val and self.isSameNode(node_1.left, node_2.left) and self.isSameNode(node_1.right, node_2.right):
            return True
        return False