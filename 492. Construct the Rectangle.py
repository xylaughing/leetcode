class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """

        """
        n = int(ceil(sqrt(area)))
        if n*n == area:
            return [n, n]
        while n <= area:
            if area % n == 0:
                return [n, area/n]
            n += 1        
        """
        # much faster
        n = int(sqrt(area))
        while n > 0:
            if area % n == 0:
                return [area/n, n]
            n -= 1
