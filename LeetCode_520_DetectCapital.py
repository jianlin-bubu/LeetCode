#https://leetcode.com/problems/detect-capital/description/
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        from string import *
        lowercase = ascii_lowercase
        uppercase = ascii_uppercase
        word_list = list(word)
        for index, word in enumerate(word_list):
            if word in lowercase:
                word_list[index] = 'lowercase'
            else:
                word_list[index] = 'uppercase'
        if len(set(word_list)) == 1:
            return True
        elif word_list[0] == 'uppercase' and word_list[1] == 'lowercase' and len(set(word_list[1:])) == 1:
            return True
        else:
            return False
        
