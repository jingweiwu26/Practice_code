# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 18:34:23 2017

@author: Wu Jingwei
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        first=head.next
        second=head.next.next
        while first and second:
            if first==second:
                return True
            if not second.next:
                return False
            first=first.next
            second=second.next.next
        return False