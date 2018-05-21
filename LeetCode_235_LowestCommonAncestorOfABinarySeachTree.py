#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pointer = root
        while pointer:
            if pointer.val > p.val and pointer.val > q.val:
                pointer = pointer.left
            elif pointer.val < p.val and pointer.val < q.val:
                pointer = pointer.right
            else:
                return pointer






        
