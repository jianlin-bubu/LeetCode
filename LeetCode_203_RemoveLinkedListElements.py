#https://leetcode.com/problems/remove-linked-list-elements/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return head
        dummy = ListNode(None)
        pre = dummy
        pre.next = head
        cur = head
        while cur:
            if cur.val == val:
                print 1
                cur = cur.next
                pre.next = None
            else:
                pre.next = cur
                pre = pre.next
                cur = cur.next
        return dummy.next

