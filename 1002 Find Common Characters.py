class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = collections.Counter(words[0])
        for i in range(1, len(words)):
            res = res & collections.Counter(words[i])
            if not res: break

        return  res.elements()
        
