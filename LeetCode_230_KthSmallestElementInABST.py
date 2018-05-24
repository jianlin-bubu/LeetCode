#https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def tranversal(root):
            if root:
                return tranversal(root.left) + [root.val] + tranversal(root.right)
            return []

        l = tranversal(root)
        l.sort()
        return l[k-1]










