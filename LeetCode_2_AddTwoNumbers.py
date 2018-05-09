#https://leetcode.com/problems/add-strings/description/
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        IntConverter = lambda x: ord(x) - ord('0')

        num1, num2 = list(map(IntConverter, num1[::-1])), list(map(IntConverter, num2[::-1]))

        if len(num1) < len(num2):
            num1, num2 = num2, num1

        carry = 0
        final_result = []
        for i in range(len(num1)):
            if i < len(num2):
                n = num2[i]
            else:
                n = 0
            tmp = n + num1[i] + carry
            carry = tmp // 10
            final_result.append(tmp % 10)
        print final_result

        if carry:
            final_result.append(1)
        return ''.join(str(x) for x in final_result[::-1])
        #equivalent: return ''.join(map(str, final_result[::-1]))












