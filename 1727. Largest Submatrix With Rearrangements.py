class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        """
        84. Largest Rectangle in Histogram
        85. Maximal Rectangle
        """
        # build the histogram for each position
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1 and i > 0:
                    matrix[i][j] += matrix[i-1][j]
        # rearrange the histogram as decreasing order            
        histogram = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        maxs = 0
        for r in range(len(matrix)):
            histogram[r] = sorted(matrix[r], reverse = True)
            maxs = max(maxs, max([histogram[r][c] * (c+1) for c in range(len(matrix[0]))]))
        return maxs
