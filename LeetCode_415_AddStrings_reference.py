#https://leetcode.com/problems/add-strings/description/
#reference 
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def _convertInter(num):
            return ord(num) - ord('0')
        # 将两个字符串逆序后，转换为list，这里题目有要求，不能使用库函数直接把string转换为int，需要我们自己实现一个字符串转换数字的函数。调转的好处是可以从个位数开始加起来
        num1, num2 = list(map(_convertInter, num1[::-1])), list(map(int, num2[::-1]))

        # 如果num2的长度 大于 num1，交换它们的顺序。
        if len(num1)<len(num2):
            num1, num2 = num2, num1

        # n代表要跟num1[i]相加的数字，主要解决两个数字length不一样的问题
        # tmp代表num1和num2同一个位置上的数字相加的结果
        # tmp的个位数会update在num1上面，求法就是去tmp的个位数
        # tmp的十位数就是carry
        carry = 0
        for i in range(len(num1)):
            n = num2[i] if i<len(num2) else 0 # 较短的那一位如果不够，则该位补0
            tmp = n + carry + num1[i] # 有进位，则将进位加上
            num1[i] = tmp % 10
            carry = tmp // 10

        # 最后存在进位，记得将这个进位加上。
        if carry:
            num1.append(1)
        # 这里没有要求不能将integer转换为str，所以直接使用了内建函数str()
        return ''.join(map(str, num1))[::-1]

# 作者：如烟花非花
# 链接：https://www.jianshu.com/p/e17ce9759fa7
# 來源：简书
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。









                
