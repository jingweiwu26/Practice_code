# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 16:52:41 2018

@author: Wu Jingwei
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res=[]
        current=head
        while current:
            res.append(current.val)
            current = current.next
        l=ListNode(-1)
        current=l
        for i in sorted(res):
            current.next=ListNode(i)
            current = current.next
        return l.next