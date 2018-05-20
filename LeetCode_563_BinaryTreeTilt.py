#https://leetcode.com/problems/binary-tree-tilt/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sums = {}
        sums[None] = 0
        def getSum(root):
            if root:
                sums[root] = getSum(root.left) + getSum(root.right) + root.val
                return sums[root]
            return 0
        getSum(root)

        def getTilt(node, sums):
            if node:
                root_tilt = abs(sums[node.left] - sums[node.right])
                return root_tilt + getTilt(node.left, sums) + getTilt(node.right, sums)
            return 0

        return getTilt(root, sums)
