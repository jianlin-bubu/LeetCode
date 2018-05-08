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
        """
        #equivalent
        def letter_to_morse_def(x):
            return morse_code[ord(x) - ord('a')]
        """
        #word to morse
        word_to_morse = lambda word: ''.join([letter_to_morse(x) for x in word])
        """
        #equivalent:
        def word_to_morse_def(word):
            l = []
            for x in word:
                l.append(letter_to_morse(x))
            return ''.join(l)
        """
        #all words to morse
        words_to_morse = map(word_to_morse, words)
        #equivalent: words_to_morse = [word_to_morse(word) for word in words]
        """
        #equivalent:
        l_words = []
        for  word in words:
            a = word_to_morse_def(word)
            l_words.append(a) #equivalent: l += [a]
        """
        #unique
        return len(set(words_to_morse))

