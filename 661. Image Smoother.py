class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(img), len(img[0])      
        res = [[0]*n for i in range(m)]
        direc = ((0,0), (0,1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1))                                          
        for i in range(m):
            for j in range(n):
                temp = [img[i+r][j+c] for r, c in direc if 0 <= i+r < m and 0 <= j+c < n]
                res[i][j] = sum(temp) // len(temp)
        return res
