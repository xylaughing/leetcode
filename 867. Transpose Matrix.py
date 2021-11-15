class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        """
        output = []
        for c in range(len(matrix[0])):
            output.append([matrix[r][c] for r in range(len(matrix))])
        return output
        """
        return zip(*matrix)
