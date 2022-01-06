class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        stops = [0] * 1001
        for [num, fro, to] in trips:
            stops[fro] += num
            stops[to] -= num
        passincar = 0
        for i in range(0, 1001):
            passincar += stops[i]
            if passincar > capacity:
                return False
        return True
