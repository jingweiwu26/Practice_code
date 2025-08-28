# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 23:27:31 2017

@author: Wu Jingwei
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        mapping={}
        current=head
        while current:
            if id(current) in mapping:
                return current
            mapping[id(current)]=current.val
            current=current.next
        return None
        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        f = s = head
        while f and f.next:
            f = f.next.next
            s = s.next
            
            if f == s:
                s = head
                while f != s :
                    s = s.next
                    f = f.next
                return f
        
        return None