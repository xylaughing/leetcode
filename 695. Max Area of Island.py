class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        def dfs(grid, i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = 0
                return 1 + dfs(grid, i-1, j) + dfs(grid, i+1, j) + dfs(grid, i, j-1) + dfs(grid, i, j+1)
            return 0
        
        res = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res.append(dfs(grid, i, j))
        return max(res) if res else 0
