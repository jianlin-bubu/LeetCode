#https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
#reference: http://www.eazow.com/2017/07/31/LeetCode-637-Average-of-Levels-in-Binary-Tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        # reference: http://www.eazow.com/2017/07/31/LeetCode-637-Average-of-Levels-in-Binary-Tree/
        sums = []
        nums = []
        def dfs(node, level):
            if node:
                # 先定位node在哪一层
                if len(sums) <= level:
                    # 这样做的好处是什么：让每一个level上的都有一个值先，过后方便以level做为index来变更
                    sums.append(0)
                    nums.append(0)

                # 计算每一层的总数和node的个数。这里通过level做为index
                sums[level] += node.val
                nums[level] += 1

                dfs(node.left, level+1)
                dfs(node.right, level+1)
        # 从root开始运行，trigger recursion
        dfs(root, 0)

        result = []
        for i in range(len(sums)):
            result.append(sums[i]/float(nums[i]))

        return result


