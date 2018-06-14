# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        current=[root]
        result=[]
        revert_flag=False
        while current:
            current_val=[root.val for root in current]
            next=[]
            for root in current:
                if root.left:
                    next.append(root.left)
                if root.right:
                    next.append(root.right)
            if revert_flag:
                    current_val=list(reversed(current_val))
            revert_flag=not revert_flag
            result.append(current_val)
            current=next
        return result

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
    
        res = []
        order = True
        current = [root]
        while current:
            next = []
            l = [node.val for node in current] if order else [node.val for node in current[::-1]]
            order = False if order else True
            res.append(l)
            for node in current:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            current = next
        return res
