class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        remainder = [None]
        right_dic = {')':'(',']':'[','}':'{'}
        for i in s:
            if i in right_dic and right_dic[i] == remainder[-1]:
                remainder.pop()
            else:
                remainder.append(i)
        return len(remainder) == 1
