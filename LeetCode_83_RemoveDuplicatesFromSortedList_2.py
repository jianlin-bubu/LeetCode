#https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
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
        pre = pre.next
        cur = head.next
        while cur:
            if pre.val == cur.val:
                cur = cur.next
                pre.next = None
            else:
                pre.next = cur
                cur = cur.next
                pre = pre.next
        return dummy.next
            
        
        
            
