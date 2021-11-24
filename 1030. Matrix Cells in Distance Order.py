class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        dic = {}
        for i in range(rows):
            for j in range(cols):
                distance = abs(i-rCenter) + abs(j-cCenter)
                dic[(i, j)] = distance 
        return sorted(dic, key=lambda x : dic[x])
