#https://leetcode.com/problems/maximum-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        max_val = max(nums)
        max_val_index = nums.index(max_val)
        left = nums[:max_val_index]
        right = nums[max_val_index+1:]
        root = TreeNode(max_val)
        root.left = self.constructMaximumBinaryTree(left)
        root.right = self.constructMaximumBinaryTree(right)
        return root

