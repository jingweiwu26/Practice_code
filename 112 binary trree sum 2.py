# -*- coding: utf-8 -*-
"""
Created on Tue Sep 05 23:50:03 2017

@author: Wu Jingwei
"""

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
        ans=[]
        self._pathSum(root, sum, [], ans)
        return ans

    def _pathSum(self, root, sum, cur, ans):
        if not root:
            return 
        if not root.left and not root.right and root.val==sum:
            cur.append(root.val)
            ans.append(cur)
        sub_sum=sum-root.val
        if root.left:
            self._pathSum(root.left, sub_sum, cur + [root.val], ans)
        if root.right:
            self._pathSum(root.right, sub_sum, cur + [root.val], ans)
            
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def backtrack(n, t):
            
            if not n: return False
            
            if t==n.val and n.left is None and n.right is None:return True
            
            if n.left is None and n.right is None: return False
            
            if backtrack(n.left, t-n.val): return True
            if backtrack(n.right, t-n.val):
                return True
            return False
        
        return backtrack(root, targetSum)
            
