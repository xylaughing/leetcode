class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        output = []
        fr, lc, lr, fc = 0, len(matrix[0])-1, len(matrix)-1, 0
        while fr < lr and fc < lc:
            output += matrix[fr][fc:lc+1]
            output += [matrix[i][lc] for i in range(fr+1, lr)]
            output += matrix[lr][fc:lc+1][::-1]
            output += [matrix[i][fc] for i in range(lr-1, fr, -1)]
            fr, lc, lr, fc = fr+1, lc-1, lr-1, fc+1
        if fr == lr:
            output.extend(matrix[fr][fc:lc+1])
        elif fc == lc:
            output += [matrix[i][fc] for i in range(fr, lr+1)]
        return output
