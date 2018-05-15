#https://leetcode.com/problems/add-two-numbers-ii/description/
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

        length_l1 = self.listLength(l1)
        length_l2 = self.listLength(l2)
        if length_l1 > length_l2:
            l1, l2 = l2, l1
        root_l1 = l1
        root_l2 = l2
        l3 = ListNode(0)
        root_l3 = l3
        count = 0
        while count < (abs(length_l1 - length_l2)):
            root_l3.next = ListNode(0)
            root_l3 = root_l3.next
            count += 1
        root_l3.next = root_l1
        root_l1 = l3.next

        carry = self.computeAndCarry(root_l1,root_l2) # 抓住carry
        if carry != 0:
            new_head = ListNode(carry)
            new_head.next = l2
            l2 = new_head
        return l2


    def listLength(self,l):
        cur = l
        length = 0
        while cur:
            length += 1
            cur = cur.next
        return length

    def computeAndCarry(self, l1, l2):
        if l1 == None and l2 == None: # 这里可以防止l1.next跟l2.next等于none的情况； 这里应该使用if，而不是while
            return 0
        l2.val = l2.val + l1.val + self.computeAndCarry(l1.next, l2.next)
        carry = l2.val // 10
        l2.val = l2.val % 10
