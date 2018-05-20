#https://leetcode.com/problems/binary-tree-preorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # root, left, right
        result = []
        def dfs(node, result):
            if node:
                result.append(node.val)
                dfs(node.left, result)
                dfs(node.right, result)

        dfs(root, result)
        return result

