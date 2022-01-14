class Solution(object):
    def helper(self, board, i, j, word):
        if not word: 
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
            return False
        temp = board[i][j]
        board[i][j] = "&"       # change the cell in case searched again
        res = self.helper(board, i+1, j, word[1:]) or self.helper(board, i-1, j, word[1:]) or self.helper(board, i, j+1, word[1:]) or self.helper(board, i, j-1, word[1:])
        board[i][j] = temp
        return res
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board: return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, i, j, word):
                    return True           
        return False
            
