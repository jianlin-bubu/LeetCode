#https://leetcode.com/problems/odd-even-linked-list/description/
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
        if head == None:
            return head
        o = oh = head
        e = eh = head.next
        while e and e.next:
            o.next = e.next
            o = o.next
            e.next = o.next
            e = e.next
        o.next = eh
        return oh









