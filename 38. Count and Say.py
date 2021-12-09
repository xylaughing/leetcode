class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1: 
            return "1"
        arr = self.countAndSay(n-1)
        i, res, qty = 0, "", 1
        while i < len(arr)-1:
            if arr[i] == arr[i+1]:
                qty += 1
            else: 
                res += str(qty) + arr[i]
                qty = 1
            i += 1
        res += str(qty) + arr[i]
        return res
