#https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
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
        if head == None:
            return head

        l = self.length(head)
        n = l - n
        dummy = ListNode(None)
        d = dummy
        cur = head
        d.next = cur
        count = 0
        while count != n:
            count += 1
            d = d.next
        d.next = d.next.next
        return dummy.next




    def length(self, head):
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count
