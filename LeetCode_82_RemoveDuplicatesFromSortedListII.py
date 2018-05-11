#https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
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

        dummy=ListNode(0)
        pre = dummy
        pre.next=head
        cur=pre.next

        while cur!=None:
            while cur.next and cur.next.val==pre.next.val:
                cur=cur.next
            if pre.next==cur:
                pre=pre.next
            else:
                pre.next=cur.next
            cur=cur.next
        return dummy.next








