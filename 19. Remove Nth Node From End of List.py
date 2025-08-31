# -*- coding: utf-8 -*-
"""
Created on Wed Feb 07 00:20:17 2018

@author: Wu Jingwei
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        prev=None
        current=head
        cur_list=[]
        while current:
            cur_list.append(current)
            prev=current
            current=current.next
        size=len(cur_list)
        target_node = cur_list[-n]
        if target_node == head:
            head=head.next
        else:
            prev_node = cur_list[-n-1]
            prev_node.next=prev_node.next.next
        return head

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        lis = []
        res = head
        while head:
            lis.append(head)
            head = head.next
        target = lis[-n]
        if res == target:
            res = res.next
        else:
            lis[-n-1].next = lis[-n-1].next.next
        return res
        
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        t = self.find_nth_from_end(dummy, n)
        t.next = t.next.next
        return dummy.next

    def find_nth_from_end(self, head, n):
        p1 = head
        for i in range(n+1):
            p1 = p1.next
        p2 = head
        while p1:
            p1 = p1.next
            p2 = p2.next
        return p2
            
        