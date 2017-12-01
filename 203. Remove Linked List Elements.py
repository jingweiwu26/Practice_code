# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        current = head
        previous = None
        while current:
            if current.val == val:
                if current == head:
                    head = current.next
                    current = current.next
                else:
                    previous.next=current.next
                    current=current.next
            else:
                previous = current
                current = current.next
        return head