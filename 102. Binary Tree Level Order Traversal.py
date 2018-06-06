# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
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
        return result

    # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        cur = [root]
        while cur:
            res.append([node.val for node in cur])
            next = []
            for node in cur:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            cur = next
        return res
