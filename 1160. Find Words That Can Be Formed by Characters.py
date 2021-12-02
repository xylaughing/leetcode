class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        res = 0
        char_dic = Counter(chars)
        for word in words:
            if not Counter(word) - char_dic:
                res += len(word)
        return res
