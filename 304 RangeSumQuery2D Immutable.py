class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.acu = [[0 for i in range(len(matrix[0]) +1) ] for j in range(len(matrix)+1)]       
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                self.acu[i][j] = matrix[i-1][j-1] + self.acu[i][j-1] + self.acu[i-1][j] - self.acu[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """     
        return self.acu[row2+1][col2+1] + self.acu[row1][col1] - self.acu[row1][col2+1] - self.acu[row2+1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
