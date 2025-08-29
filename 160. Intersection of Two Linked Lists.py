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
        dic = {}
        cur = headA
        while cur:
            dic[id(cur)] = cur.val
            cur = cur.next
        cur = headB
        while cur:
            if id(cur) in dic:
                return cur
            cur = cur.next
        return 
        
        
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pa = headA
        pb = headB
        while pa != pb:
            pa=pa.next if pa else headB
            pb= pb.next if pb else headA
        return pa
