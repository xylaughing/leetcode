class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def dfs(board, i, j):
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'I'
                dfs(board, i-1, j)
                dfs(board, i+1, j)
                dfs(board, i, j-1)
                dfs(board, i, j+1)
        
        # change the boarder 'O' to 'I' and check its surroundings. 
        for i in [0, m-1]:
            for j in range(n):
                dfs(board, i, j)
        for j in [0, n-1]:
            for i in range(1, m-1):
                dfs(board, i, j)
        # change it back
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'I':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        return
