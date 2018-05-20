#https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root == None:
            return False
        
        nodes = []
        def getNodes(node, nodes):
            if node:
                nodes.append(node)
                getNodes(node.left, nodes)
                getNodes(node.right, nodes)
        getNodes(root, nodes)
        
        def getResult(node, nodes, k):
            if node:
                for n in nodes:
                    if n != node and n.val + node.val == k:
                        return True
                return getResult(node.left, nodes, k) or getResult(node.right, nodes, k)
            return False
            
        return getResult(root, nodes, k)
        
