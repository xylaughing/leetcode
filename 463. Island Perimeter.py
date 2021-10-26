class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        """        
        dup = 0
        l, w = len(grid), len(grid[0])
        for i in range(l):
            for j in range(w):
                if j<w-1 and grid[i][j] == grid[i][j+1] == 1:
                    dup += 1
                if i<l-1 and grid[i][j] == grid[i+1][j] == 1:
                    dup += 1
        return  sum([sum(x) for x in grid]) * 4 - 2* dup
        """
        
        """
        grid_ext = ['0' + ''.join(str(x) for x in row) + '0' for row in grid]
        grid_trans = list(map(list, zip(*grid)))
        grid_ext += [ '0' + ''.join(str(x) for x in row) + '0' for row in grid_trans ] 
        return sum(row.count('01') + row.count('10') for row in grid_ext)
        """
        
        area = 0
        for row in grid + list(map(list, zip(*grid))):
            for i1, i2 in zip([0] + row, row + [0]):
                area += int(i1 != i2)
        return area        
"""
zip(*grid): transform of grid
grid + list(map(list,zig(*grid))): grid appended grid_trans
('grid+trans', [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0], [0, 1, 0, 1], [1, 1, 1, 1], [0, 1, 0, 0], [0, 0, 0, 0]])
zip([0] + row, row + [0]): giving the ext liners
1('zip [0]', [(0, 0), (0, 1), (1, 0), (0, 0), (0, 0)])
2('zip [0]', [(0, 1), (1, 1), (1, 1), (1, 0), (0, 0)])
3('zip [0]', [(0, 0), (0, 1), (1, 0), (0, 0), (0, 0)])
4('zip [0]', [(0, 1), (1, 1), (1, 0), (0, 0), (0, 0)])
5('zip [0]', [(0, 0), (0, 1), (1, 0), (0, 1), (1, 0)])
6('zip [0]', [(0, 1), (1, 1), (1, 1), (1, 1), (1, 0)])
7('zip [0]', [(0, 0), (0, 1), (1, 0), (0, 0), (0, 0)])
8('zip [0]', [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)])
"""
