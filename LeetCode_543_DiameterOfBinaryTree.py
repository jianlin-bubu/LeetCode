#https://leetcode.com/problems/diameter-of-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def depth(root):
            if root == None:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            self.res = max(self.res, left+right)
            return max(left, right) + 1

        depth(root)
        return self.res









