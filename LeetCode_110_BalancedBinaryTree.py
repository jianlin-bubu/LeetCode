#https://leetcode.com/problems/balanced-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def depth(root):
            if root == None:
                return 0
            return max(depth(root.left) + 1, depth(root.right) + 1)


        if root == None:
            return True
        depth_left = depth(root.left)
        depth_right = depth(root.right)
        if abs(depth_left - depth_right) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False



