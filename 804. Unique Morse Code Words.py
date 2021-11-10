class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        # ord('a') = 97
        wordset = set(words)
        if len(wordset) == 1: return 1
        codeset = []
        for word in wordset:
            temp = ''.join(table[ord(x)-97] for x in word)
            if temp not in codeset:
                codeset.append(temp)
        return len(codeset)
