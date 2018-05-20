#https://leetcode.com/problems/most-frequent-subtree-sum/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        sums = []
        # 这个function的目的是给一个点可以return subtree sum，那就以为这我必须return我
        def findAllTreeSum(root, sums):
            if root == None:
                return 0
            # if root.left == None and root.right != None:
            #     s_right = findAllTreeSum(root.right, sums)
            #     sums.append(s_right + root.val)
            #     return sums
                  #这是一个错误写法，正确写法是上面的三行(原因：因为我这样没有return任何东西所以这里就不能使用findAllTreeSum(root.right, sums))
                  # sums.append(findAllTreeSum(root.right, sums) + root.val) #
            # elif root.left != None and root.right == None:
            #     sums.append(findAllTreeSum(root.left, sums) + root.val)
            # elif root.left == None and root.right == None:
            #     sums.append(root.val)
            # else:
            #     sums.append(root.val + findAllTreeSum(root.left, sums) + findAllTreeSum(root.right, sums))
            s = findAllTreeSum(root.left, sums) + findAllTreeSum(root.right, sums) + root.val
            sums.append(s)
            return s

        findAllTreeSum(root, sums)

        dic = {}
        largest = 0
        for i in sums:
            if i not in dic:
                dic[i] = 1
            dic[i] += 1
            if dic[i] >= largest:
                largest = dic[i]
        result = []
        for i in dic:
            if dic[i] == largest:
                result += [i]
        return result








