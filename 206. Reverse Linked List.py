# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        prev = None

        if not head:
            return head
        while current:
            _next = current.next
            current.next=prev
            prev = current
            current = _next

        return prev
    
  class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        prev = None
        while current:
            _ = current.next
            current.next = prev
            prev = current
            current = _
        return prev
