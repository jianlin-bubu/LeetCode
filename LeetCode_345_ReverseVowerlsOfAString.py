class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowel = "aeiou"
        left, right = 0, len(s)-1
        while left < right:
            if s[left].lower() not in vowel:
                left += 1
            elif s[right].lower() not in vowel:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return "".join(s)
            
                    
                



