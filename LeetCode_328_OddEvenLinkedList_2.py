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
        dummy_odd = ListNode(None)
        do = dummy_odd
        dummy_even = ListNode(None)
        de = dummy_even
        cur = head
        while cur:
            do.next = cur
            cur = cur.next
            do = do.next
            do.next = None
            if cur != None:
                de.next = cur
                cur = cur.next
                de = de.next
                de.next = None
        do.next= dummy_even.next
        return dummy_odd.next








