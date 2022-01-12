class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n-1
        while r <= m - 1 and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1
            else:
                r += 1
            #print(r, c, matrix[r][c])
        return False
