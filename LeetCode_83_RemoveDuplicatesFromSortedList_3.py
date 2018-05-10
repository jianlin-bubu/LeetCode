#https://leetcode.com/submissions/detail/153492987/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        dummy = ListNode(None)
        pre = dummy
        pre.next = head
        while head:
            if head.next and head.val == head.next.val:
                head = head.next
            else:
                pre.next = head
                pre = pre.next
                head = head.next
        return dummy.next



