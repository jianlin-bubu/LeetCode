#https://leetcode.com/problems/unique-morse-code-words/description/
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        def LetterToMorse(letter):
            return morse_code[ord(letter) - ord('a')]

        #word to morse
        def WordToMorse(word):
            MorseWord = ''.join(map(LetterToMorse, word))
            return MorseWord

        #words to morse
        def WordsToMorse(words):
            MorseWords = map(WordToMorse, words)
            return len(set(MorseWords))

        return WordsToMorse(words)









