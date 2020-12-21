# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 13:52:37 2017

@author: Wu Jingwei
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        head_node=ListNode(0)
        l=head_node
        carry=0
        while l1 or l2 or carry:
            sum, carry=carry, 0
            if l1:
                sum+=l1.val
                l1=l1.next
            if l2:
                sum+=l2.val
                l2=l2.next
            if sum>9:
                carry+=1
                sum-=10
            l.next=ListNode(sum)
            l=l.next
        return head_node.next
    
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = ListNode(-1)
        cur = head
        current_l1 = l1
        current_l2 = l2
        while current_l1 or current_l2:
            if not current_l1:
                current_l1 = ListNode(0)
            if not current_l2:
                current_l2 = ListNode(0)
            val = current_l1.val + current_l2.val + carry
            carry = 0
            if val >9:
                carry += 1
                val -= 10
            node = ListNode(val)
            cur.next = node
            cur = node
            current_l1 = current_l1.next
            current_l2 = current_l2.next
        if carry:
            cur.next = ListNode(carry)
        return head.next
    
    class Solution:
        def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
            head = ListNode(0)
            carry = 0
            cursor = head

            while l1 or l2 or carry:
                val = (l1.val if l1 is not None else 0) + (l2.val if l2 is not None else 0) + carry
                carry = 0
                if val >= 10:
                    val = val % 10
                    carry = 1
                node = ListNode(val)
                head.next = node
                if l1 is not None:
                    l1 = l1.next
                if l2 is not None:
                    l2 = l2.next
                head = head.next
            return cursor.next
