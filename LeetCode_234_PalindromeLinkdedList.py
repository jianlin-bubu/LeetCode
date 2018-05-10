#https://leetcode.com/problems/palindrome-linked-list/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        l = []
        while head:
            l += [head.val]
            head = head.next
        if l == l[::-1]:
            return True
        return False




