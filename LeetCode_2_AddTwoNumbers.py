#https://leetcode.com/submissions/detail/153413398/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        result = []
        while l1 != None and l2 != None:
            tmp = l1.val + l2.val + carry
            carry = tmp // 10
            result.append(tmp % 10)
            l1 = l1.next
            l2 = l2.next
        while l1 == None and l2 != None:
            tmp = l2.val + carry
            carry = tmp // 10
            result.append(tmp % 10)
            l2 = l2.next
        while l1 != None and l2 == None:
            tmp = l1.val + carry
            carry = tmp // 10
            result.append(tmp % 10)
            l1 = l1.next
        if l1 == None and l2 == None:
            if carry != 0:
                result.append(1)
        return result
            
            
