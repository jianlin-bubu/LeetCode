#https://leetcode.com/problems/subtree-of-another-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        def isSameTree(s, t):
            if s == None and t == None:
                return True
            if s == None or t == None:
                return False
            return isSameTree(s.left, t.left) and s.val == t.val and isSameTree(s.right, t.right)

        # 为什么需要这一句，isSameTree不是已经有了吗？ 只要用是不是就可以？：这两句相当于guard，当s是None，而t不是None的时候，如果没有这两句，就会出现return False的情况，然后就会进入到‘return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)’就会出问题
        if s is None or t is None:
            return s is None and t is None
        if isSameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        # 为什么最后这一句不可以写做这样：因为只是匹配了三个头，root, roo.left，root.right，然后就结束了。
        # return isSameTree(s.left, t) or isSameTree(s.right, t)

        # alternative
        # if s == None and t == None:
        #     return True
        # if s == None or t == None:
        #     return False
        # if s:
        #     if self.isSubtree(s.left, t) or self.isSubtree(s.right, t) or isSameTree(s, t):
        #         return True
        #     return False





