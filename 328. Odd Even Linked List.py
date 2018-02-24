# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 13:02:22 2018

@author: Wu Jingwei
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """


        odd_list_dummy_head = ListNode(-1)
        even_list_dummy_head = ListNode(-1)
        current_odd, current_even = odd_list_dummy_head, even_list_dummy_head

        current = head
        is_odd = False
        while current:
            is_odd = not(is_odd)
            if is_odd:
                current_odd.next = current
                current_odd = current
            else:
                current_even.next = current
                current_even = current
            current = current.next
        current_odd.next = even_list_dummy_head.next
        current_even.next = None
        return odd_list_dummy_head.next