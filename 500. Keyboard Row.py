class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        """
        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set('zxcvbnm')
        res = []
        for w in words:
            temp = set(w.lower())
            if temp <= row1 or temp <= row2 or temp <= row3:
                res.append(w)
        return res
        """
        row1, row2, row3 = 'qwertyuiop', 'asdfghjkl', 'zxcvbnm'
        dic, res = {}, []
        for x in row1: dic[x] = 0b001
        for x in row2: dic[x] = 0b010
        for x in row3: dic[x] = 0b100                   
        
        for w in words:
            temp = 0b111
            for c in w.lower():
                temp = temp & dic[c]
            if temp == 0b001 or temp == 0b010 or temp == 0b100:
                res.append(w)
        return res
