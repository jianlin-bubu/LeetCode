#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        #判断某个点是不是在某个subtree上
        def treeHaveNode(root, node):
            if root == None:
                return False

            left = treeHaveNode(root.left, node)
            right = treeHaveNode(root.right, node)
            return left or right or root == node


        # 这样写不可以，因为l是一个在外部的东西，那当我执行self.lowestCommonAncestor(root.left, p, q)这一句的时候，其实它只是在一个空的l里面加东西。导致所有符合条件的nodes不是叠加在一起
        # l = []
        # 不可以用while因为会陷入死循环
        # while treeHaveNode(root, p) and treeHaveNode(root, q):
        #     l += [root.val]
            # 这样写是不行的，因为这样结果并没有抓住， l是外面的东西，里面是不会知道的
            # self.lowestCommonAncestor(root.left, p, q)
            # self.lowestCommonAncestor(root.right, p, q)
        # return l[-1]

        #更改的方法是增加一个argument是l

        l = []
        def helper(root, p, q, l):
            if treeHaveNode(root, p) and treeHaveNode(root, q):
                l += [root.val]
                helper(root.left, p, q, l)
                helper(root.right, p, q, l)
            return l[-1]

        return helper(root, p, q, l)

