#https://leetcode.com/problems/partition-list/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None:
            return head
        dummy_l = ListNode(None)
        dummy_s = ListNode(None)
        l = dummy_l
        s = dummy_s
        cur = head
        while cur:
            if cur.val < x:
                s.next = cur
                l.next = None
                cur = cur.next
                s = s.next
            else:
                l.next = cur
                s.next = None
                cur = cur.next
                l = l.next
        s.next = dummy_l.next
        return dummy_s.next






