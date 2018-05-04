class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        letters = ""
        for i in s:
            if i.isalnum():
                letters += i
        letters = letters.lower()
        return letters == letters[::-1]
    
        
                           
