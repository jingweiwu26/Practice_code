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