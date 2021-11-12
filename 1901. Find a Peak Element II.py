class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        """
        for i in range(len(mat)):
            maxR = mat[i].index(max(mat[i]))
            if i==0 and mat[i][maxR] > mat[i+1][maxR] or i == len(mat)-1 and mat[i][maxR] > mat[i-1][maxR] or mat[i][maxR] > mat[i-1][maxR]  and mat[i][maxR] > mat[i+1][maxR]:
                return [i, maxR]
        """
        lC, rC = 0, len(mat[0])-1
        while lC <= rC:
            maxR = 0
            midC = (lC + rC) / 2
            for i in range(len(mat)):
                if mat[i][midC] > mat[maxR][midC]:
                    maxR = i
            print(maxR, midC)
            if midC-1 >= lC and mat[maxR][midC] < mat[maxR][midC-1]:
                rC = midC - 1
            elif midC+1 <= rC and mat[maxR][midC] < mat[maxR][midC+1]:
                lC = midC + 1
            else:
                return [maxR, midC]
