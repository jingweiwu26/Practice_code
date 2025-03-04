# -*- coding: utf-8 -*-
"""
Created on Tue Sep 05 23:51:07 2017

@author: Wu Jingwei
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if root.val==sum and not root.left and not root.right:
            return True
        else:
            sub_sum=sum-root.val            
            return self.hasPathSum(root.left, sub_sum) or self.hasPathSum(root.right, sub_sum)
        
 # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        path = [root.val]
        self.helper(root, sum, res, path)
        return res
    
    def helper(self, node, sum, res, path):
        if not node:
            return
        sum -= node.val
        if sum == 0 and not node.left and not node.right:
            res.append(path)
        else:
            if node.left:
                self.helper(node.left, sum, res, path+[node.left.val])
            if node.right:
                self.helper(node.right, sum, res, path+[node.right.val])

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def backtrack(p, n, t):
            
            if not n: return
            p.append(n.val)
            t-= n.val
            if t==0 and not n.left and not n.right:
                res.append(p[:])

            backtrack(p, n.left, t)
            backtrack(p, n.right, t)
            p.pop()  
            
        backtrack([], root, targetSum)
        return res