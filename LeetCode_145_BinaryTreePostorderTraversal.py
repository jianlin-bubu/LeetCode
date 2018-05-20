#https://leetcode.com/problems/binary-tree-postorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def dfs(node, result):
            if node:
                dfs(node.left, result)
                dfs(node.right, result)
                result.append(node.val)
        dfs(root, result)
        return result




