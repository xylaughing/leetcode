class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        """
        res = 0
        for x in stones:
            if x in jewels:
                res += 1
        return res
        """"""
        return sum(Counter(stones)[x] for x in jewels)
        """"""
        return sum(map(stones.count, jewels))
        """        
        # faster solution
        return sum(x in jewels for x in stones)
