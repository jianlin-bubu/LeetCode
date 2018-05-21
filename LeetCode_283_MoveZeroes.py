#https://leetcode.com/problems/move-zeroes/description/
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for num in nums:
            if num != 0:
                nums[i] = num
                # 记录这是出现的第几个非0的数，然后座位index update相应位置的数值
                i +=  1
        for y in range(i, len(nums)):
            # 补全所有的0
            nums[y] = 0







