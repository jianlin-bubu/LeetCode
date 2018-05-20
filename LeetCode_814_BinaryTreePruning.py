#https://leetcode.com/problems/binary-tree-pruning/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #给出一个点，我要检查subtree里面是不是1，如果有就return True，否则就要把node砍掉，然后return False；注意要先砍掉，因为return了就结束操作了
        #这个function是要检查有没有1，顺便砍树
        #之前我一直有个误区以为子节点才是subtree，其实root，root.left，root.right三部分加起来才是一棵subtree
        def have1(root):
            if root == None:
                return False

            left = have1(root.left)
            right = have1(root.right)
            if not left:
                root.left = None
            if not right:
                root.right = None
            return left or right or root.val == 1

        if have1(root):
            return root
        # 解决root.val = 0， 左边的树和右边的树又没有0的情况
        return None




