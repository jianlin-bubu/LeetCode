class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        def numberPattern(target):
                number = 0
                target_num_dic = {}
                pattern_in_num = []
                for i in target:
                    if i not in target_num_dic:
                        target_num_dic[i] = number
                        pattern_in_num += [target_num_dic[i]]
                        number += 1
                    else:
                        pattern_in_num += [target_num_dic[i]]
                        number += 1
                return pattern_in_num
        pattern_pattern_in_num = numberPattern(pattern)
        print pattern_pattern_in_num
        words = str.split(" ")
        words_pattern_in_num = numberPattern(words)
        print words_pattern_in_num
        if pattern_pattern_in_num == words_pattern_in_num:
            return True
        else:
            return False
