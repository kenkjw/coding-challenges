""" 002 - Add Two Numbers:
https://leetcode.com/problems/add-two-numbers/

You are given two linked lists representing two non-negative numbers. The
digits are stored in reverse order and each of their nodes contain a single
digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
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
        sum = l1.val + l2.val
        l3 = ListNode(sum if sum < 10 else sum-10)
        carry = 0 if sum < 10 else 1
        p = l1
        q = l2
        r = l3

        while p.next or q.next:
            pval = p.next.val if p.next else 0
            qval = q.next.val if q.next else 0
            sum = pval + qval + carry
            r.next = ListNode(sum if sum < 10 else sum-10)
            carry = 0 if sum < 10 else 1

            p = p.next or p
            q = q.next or q
            r = r.next

        if carry:
            r.next = ListNode(1)
        return l3
