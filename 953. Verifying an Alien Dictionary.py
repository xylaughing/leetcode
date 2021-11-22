class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        
        self.dic = {j : i for i, j in enumerate(order)}
                
        def isSorted(w1, w2):
            l = min(len(w1), len(w2))
            for i in range(l):
                if self.dic[w1[i]] < self.dic[w2[i]]:
                    return True
                elif self.dic[w1[i]] > self.dic[w2[i]]:
                    return False
            return True if i == len(w1)-1 else False

        """
        for i in range(len(words)-1):
            if not isSorted(words[i], words[i+1]):
                return False
        return True
        """
        
        return True if all([isSorted(x, y) for x, y in zip(words, words[1:])]) else False
