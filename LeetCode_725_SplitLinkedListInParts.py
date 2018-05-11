#https://leetcode.com/problems/split-linked-list-in-parts/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        #建立五个空的list
        ret = [None] * k
        #计算node的数量
        cur = root
        count = 0
        while cur:
            count += 1
            cur = cur.next
        #算平均每一组的数量和余数，余数会平均分给每一个组直到余数变成0
        avg, rem = count // k, count % k
        #index用来更改空的list的值
        cur = root
        index = 0
        #开始切割
        while cur:
            #tmp记住每一组的头
            tmp = cur
            pre = ListNode(None)
            pre.next = cur
            #计算每组是否已经达到平均的数量
            num = 0
            while num < avg:
                pre, cur = pre.next, cur.next
                num += 1
            #达到平均数量之后就需要分配余数
            if rem > 0:
                pre = pre.next
                cur = cur.next
                rem -= 1
            #平均数量+平均余数达到之后就切割
            pre.next = None
            #更改list
            ret[index] = tmp
            index += 1
        return ret     
