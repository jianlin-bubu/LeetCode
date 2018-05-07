#https://leetcode.com/problems/unique-morse-code-words/description/
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        #letter to morse
        letter_to_morse = lambda x: morse_code[ord(x) - ord('a')]
        #word to morse
        word_to_morse = lambda word: ''.join([letter_to_morse(x) for x in word])
        #all words to morse
        words_to_morse = map(word_to_morse, words)
        #unique
        return len(set(words_to_morse))

