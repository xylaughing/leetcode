class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.dic = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        """
        def multiply(arr, dig):
            letters = list(self.dic[dig])
            if not arr: return letters
            return [y+x for y in arr for x in letters]
        
        output = []
        for dig in digits:
            output = multiply(output, dig)
        return output
        """
        if not digits: return []
        if len(digits) == 1: return list(self.dic[digits[0]])
        # all digits except last one
        prev = self.letterCombinations(digits[:-1])
        cur = self.dic[digits[-1]]
        return [x+y for y in cur for x in prev]
