class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0: return True
        i = 0
        while i < len(flowerbed)-1:
            if flowerbed[i] == 1: i += 2
            elif flowerbed[i+1] == 1: i += 3
            else: 
                n -= 1
                i += 2
            if n == 0: return True
        if i == len(flowerbed)-1 and flowerbed[i] == 0: n -= 1
        return n == 0
