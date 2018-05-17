#https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        if root.left == None and root.right != None:
            return self.maxDepth(root.right) + 1
        if root.right == None and root.left != None:
            return self.maxDepth(root.left) + 1
        else:
            len_left = self.maxDepth(root.left) + 1
            len_right = self.maxDepth(root.right) + 1
            return max(len_left, len_right)
