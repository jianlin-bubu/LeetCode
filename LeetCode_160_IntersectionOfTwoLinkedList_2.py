#https://leetcode.com/problems/intersection-of-two-linked-lists/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        a, b = headA, headB
        while a != b:
            if a and b:
                a = a.next
                b = b.next
            if a == None and b != None:
                a = headB
                b = b.next
            if b == None and a != None:
                b = headA
                a = a.next
        return a




