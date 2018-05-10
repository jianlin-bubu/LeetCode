#https://leetcode.com/problems/intersection-of-two-linked-lists/description/
#reference:https://blog.csdn.net/coder_orz/article/details/51615444
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
        #求长度
        lenA = self.length(headA)
        lenB = self.length(headB)
        #截较长的链条，让两条链条长度相等
        if lenA > lenB:
            headA, headB = headB, headA
        for i in range(abs(lenA-lenB)):
            headB = headB.next
        #找交点
        while headA != headB:
            headA, headB = headA.next, headB.next
        return headA

    #求长度的方法
    def length(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length



