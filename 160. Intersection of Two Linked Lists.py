# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 15:10:17 2017

@author: Wu Jingwei
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        cur_a=headA
        mapping = {}
        while cur_a:
            mapping[id(cur_a)]=cur_a.val
            cur_a=cur_a.next
        cur_b=headB
        while cur_b:
            if id(cur_b) in mapping:
                return cur_b
            cur_b=cur_b.next
        return None