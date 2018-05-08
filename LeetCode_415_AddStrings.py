#https://leetcode.com/problems/add-strings/description/
#time limit exceeded
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        string_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        #num to 4 bit
        four_bit_num = lambda x: (5009-len(x))*'0'+x

        num1 = four_bit_num(num1)
        num2 = four_bit_num(num2)

        num_to_add = [num1, num2]

        #single number string to num:
        StringToNum = lambda x: num_list[string_list.index(x)]

        #number string to num list
        StringNumToNum = lambda string_number: [StringToNum(x) for x in string_number]

        num_to_add = map(StringNumToNum, num_to_add)

        for i in num_to_add:
            for index, num in enumerate(i):
                i[index] = num*10**(5009-index-1)

        result = 0
        for i in num_to_add:
            result += sum(i)
        return str(result)










