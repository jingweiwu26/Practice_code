# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:53:03 2018

@author: Wu Jingwei
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result=[]
        current = [root]
        while current:
            current_val = [root.val for root in current]
            next = []
            for root in current:
                if root.left:
                    next.append(root.left)
                if root.right:
                    next.append(root.right)
            result.append(current_val)
            current=next
        
        if not result:
            return -1
        result = sorted(list(set(reduce(lambda x,y: x+y, result) if len(result)>=2 else result[0])))
        return -1 if len(result)==1 else result[1]