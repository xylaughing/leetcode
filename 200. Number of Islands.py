class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        def dfs(grid, i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
                grid[i][j] = '2'
                dfs(grid, i-1, j)
                dfs(grid, i+1, j)
                dfs(grid, i, j-1)
                dfs(grid, i, j+1)
            else:
                return
    
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    res += 1
        return res
        
