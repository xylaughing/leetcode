class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """       
        def Ver(x, y):
            direc = -1 if x>y else 1
            for i in range(x, y+direc, direc):
                if board[i][b] == "p":
                    return 1
                elif board[i][b] == "B":
                    return 0
            return 0
        
        def Hor(x, y):
            direc = -1 if x>y else 1
            for i in range(x, y+direc, direc):
                if board[a][i] == "p":
                    return 1
                elif board[a][i] == "B":
                    return 0
            return 0
        
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    a, b = i, j
                    break
      
        return Ver(a-1, 0) + Ver(a+1, len(board)-1) + Hor(b-1, 0) + Hor(b, len(board[0])-1)
