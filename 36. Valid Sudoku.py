class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        row, col, box = [[] for i in range(9)], [[] for i in range(9)], [[] for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j].isnumeric():
                    boxind = (i//3)*3+j//3
                    if board[i][j] not in row[i] and board[i][j] not in col[j] and board[i][j] not in box[boxind]:
                        row[i].append(board[i][j])
                        col[j].append(board[i][j])
                        box[boxind].append(board[i][j])
                    else: 
                        return False          
        return True
    
