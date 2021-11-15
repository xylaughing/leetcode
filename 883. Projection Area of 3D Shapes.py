        top = sum(x > 0 for row in grid for x in row)
        front = sum([max([grid[i][j] for i in range(len(grid))]) for j in range(len(grid[0]))])
        side = sum([max(grid[i]) for i in range(len(grid))])
        return top + front + side
