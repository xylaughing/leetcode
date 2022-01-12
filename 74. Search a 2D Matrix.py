class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        """
        matrix = sum(matrix, [])
        l, r = 0, len(matrix)-1
        while l < r:
            mid = (l + r) // 2
            if matrix[mid] == target:
                return True
            elif matrix[mid] > target:
                r = mid
            else:
                l = mid + 1
        return False if matrix[l] != target else True
        """
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m*n-1
        while start < end:
            mid = (start + end) // 2
            r, c = divmod(mid, n)
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                end = mid
            else:
                start = mid + 1
        r, c = divmod(start, n)
        return False if matrix[r][c] != target else True
