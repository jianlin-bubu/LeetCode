#https://leetcode.com/problems/merge-k-sorted-lists/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        result = ListNode(None)
        r = result
        for i in range(len(lists)):
            result = self.mergeTwoLists(result, lists[i])
        return result.next

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(None)
        pre = dummy
        while l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            pre.next = l1
            pre = pre.next
            l1 = l1.next
        l1 = l1 or l2
        pre.next = l1
        return dummy.next
