#https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # get level
        # update level_largest[level]
        # 因为这个问题不需要下级返回什么东西，所以就不需要return
        # leve_largest放在def之外，要在def里面用它，所以要把它变成一个argument。一般在外面的这种，是我会在def里面修改或者添加东西的。而且有可能def本身并不需要return什么东西
        level_largest = []
        def dfs(root, level, level_largest):
            # 这是一个guard，把特殊的情况排除掉。符合一般人的写法，而且比较好读
            if root == None:
                return

            if len(level_largest) <= level:
                level_largest.append(None)
            # 以下这些是不可以退后一个层级的，因为这样会保证如果level_largest[level]被换过一次值之后还可以继续比较
            if root.val >= level_largest[level]:
                level_largest[level] = root.val
            dfs(root.left, level+1, level_largest)
            dfs(root.right, level+1, level_largest)

        dfs(root, 0, level_largest)

        return level_largest

