#https://leetcode.com/submissions/detail/153478911/
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

        pre = ListNode('0')
        dummy = pre
        pre.next = head
        dup = None
        cur = head
        while cur:
            if cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next
                dup = cur
            else:
                if cur == dup:
                    cur = cur.next
                    pre.next = cur
                else:
                    pre = cur
                    cur = cur.next
        return dummy.next








