class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        """
        seen = []
        for i in range(len(matrix)):
            temp = [ind for ind, v in enumerate(matrix[i]) if v == 0]
            if temp:
                matrix[i] = [0] * len(matrix[0])
            seen.extend(temp)
        seen = set(seen)
        for c in seen:        
            for r in range(len(matrix)):
                matrix[r][c] = 0
        """
        for i in range(len(matrix)):
            temp = [ind for ind, v in enumerate(matrix[i]) if v == 0]
            if temp:
                matrix[i] = [0] * len(matrix[0])
            for c in temp:
                for r in range(len(matrix)):
                    if matrix[r][c] !=0:
                        matrix[r][c] = 2**31
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 2**31:
                    matrix[i][j] = 0
        
