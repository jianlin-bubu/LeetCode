#https://leetcode.com/problems/linked-list-components/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        g = set(G)
        #有了这个就可以避免head.next.val
        pre = ListNode(None)
        pre.next = head
        answer = 0
        while head:
            if pre.val not in g and head.val in g:
                print 1
                answer += 1
            pre = pre.next
            head = head.next
        return answer

