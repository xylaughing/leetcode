class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(mat) * len(mat[0]) != r*c:
            return mat
        mat = sum(mat, [])
        return [mat[i*c:(i+1)*c] for i in range(r)]
            
