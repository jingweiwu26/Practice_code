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
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(n):
            if not n: return
            n.left, n.right = n.right, n.left
            dfs(n.left)
            dfs(n.right)
        
        dfs(root)
        return root
        
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var invertTree = function(root) {
    
    const dfs = function(n) {
        if (!n) {return}
        [n.left, n.right]= [n.right, n.left]
        dfs(n.left)
        dfs(n.right)
}
    dfs(root)
    return root
};

