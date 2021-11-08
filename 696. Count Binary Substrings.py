class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1: return 0
        # to get a qtyArr to represent the qty of grouped 1s and 0s
        qtyArr, qty, i = [], 1, 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                qty += 1
            else:
                qtyArr.append(qty)
                qty = 1
        qtyArr.append(qty)

        res = 0
        return sum([min(qtyArr[i], qtyArr[i+1]) for i in range(len(qtyArr)-1)])
