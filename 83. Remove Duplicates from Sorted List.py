# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        current=head
        prev=None

        while current:
            if prev and current.val==prev.val:
                prev.next=current.next
                current=current.next
            else:
                prev=current
                current=current.next
        return head