class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        front, side, top = 0, 0, 0
        # side view & front view. since m=n, index change
        for i in range(n):
            for j in range(n):
                if j == 0:
                    side += grid[i][j]
                    front += grid[j][i]
                else:
                    side += abs(grid[i][j] - grid[i][j-1])
                    front += abs(grid[j][i] - grid[j-1][i])
                if grid[i][j] !=0:
                    top += 2
            side += grid[i][j]
            front += grid[j][i]

        return side + front + top
