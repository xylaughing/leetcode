class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        def gcd(x, y):
            while y != 0:
                (x, y) = (y, x % y)
            return x
        
        if len(deck) == 1: return False
        ct = Counter(deck).values()
        # return True if all(gcd(ct[i], ct[i+1]) > 1 for i in range(len(ct)-1)) else False
        return True if reduce(gcd, ct) > 1 else False
