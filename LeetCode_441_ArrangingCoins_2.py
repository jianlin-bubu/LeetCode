#https://leetcode.com/problems/arranging-coins/description/
#version 2
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        base = 1
        if n == 0:
            return 0
        level = 0
        while n > 0:
            if n - level > 0:
                n -= level
                level += 1
            elif n - level == 0:
                return level
            else:
                n - level < 0:
                    return level - 1
                
        
        
