#https://leetcode.com/problems/reverse-linked-list-ii/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # 空或者仅仅一个节点或者不需要翻转
        if head == None or head.next == None or m == n:
            return head

        # 当m==1，即需要从第一个节点开始翻转
        if m == 1:
            count = 0
            cur = head
            pre = None
            while cur and count < n:
                count += 1
                nex = cur.next
                cur.next = pre
                pre = cur
                cur = nex
            head.next = cur
            return pre

        # 当m>1,需要把原来的linked list 切成三段再合并
        cur = head
        count = 0
        while cur:
            count += 1
            nex = cur.next
            if count == m - 1:
                first_part_end = cur
                cur.next = None
                second_part = cur = nex
            elif count == n:
                cur.next = None
                third_part = nex
            else:
                cur = cur.next
        # 调转要求的部分
        cur = second_part
        pre = None
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        # 重新组合
        first_part_end.next = pre
        second_part.next = third_part
        return head





