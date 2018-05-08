#https://leetcode.com/problems/arranging-coins/description/
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = -1
        base = 1
        if n == 1:
            return 1
        elif n == 0:
            return 0
        else:
            while n >= 0:
                n = n-base
                result += 1
                base += 1
            return result


