# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.mirror(root.left, root.right)
        
    def mirror(self, left, right):
        if not left and right:
            return False
        if not right and left:
            return False
        if not left and not right:
            return True
        if left.val != right.val:
            return False
        return self.mirror(left.left, right.right) and self.mirror(left.right, right.left)

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.helper(root.left, root.right)
    
    def helper(self, l, r):
        if not l and not r:
            return True
        if l and not r:
            return False
        if r and not l:
            return False
        if l.val != r.val:
            return False
        return self.helper(l.left, r.right) and self.helper(l.right, r.left)
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(l, r):
            if l is None and r is not None:
                return False
            elif l is not None and r is None:
                return False
            elif l is None and r is None:
                return True
            elif l.val != r.val:
                return False
            
            out_s = dfs(l.left, r.right)
            in_s = dfs(l.right, r.left)
            return out_s and in_s
        
        if not root: return
        return dfs(root.left, root.right)
            
