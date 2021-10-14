class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        uglylist = [1]
        l1, l2, l3 = 0, 0, 0
        for i in range(1, n):
            x, y, z = uglylist[l1]*2, uglylist[l2]*3, uglylist[l3]*5
            minval = min(x, y, z)
            uglylist.append(min(x, y, z))
            if minval == x:    l1 += 1
            if minval == y:    l2 += 1
            if minval == z:    l3 += 1
        return uglylist[n-1]
