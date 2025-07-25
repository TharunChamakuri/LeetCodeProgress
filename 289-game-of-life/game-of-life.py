class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        original    | new   |   state   |
            0       |  0    |    0      |
            1       |  0    |    1      |
            0       |  1    |    2      |
            1       |  1    |    3      |
        """
        row , col = len(board) , len(board[0])

        def neighCount(r,c):
            neigh = 0
            for i in range(r - 1,r + 2):
                for j in range(c - 1,c + 2):
                    if ((i == r and j == c) or i < 0 or j < 0 or
                        i == row or j == col):
                        continue
                    if board[i][j] in [1,3]:
                        neigh += 1
            return neigh

        
        for r in range(row):
            for c in range(col):
                neigh = neighCount(r,c)
                if board[r][c]:
                    if neigh in [2,3]:
                        board[r][c] = 3
                else:
                    if neigh == 3:
                        board[r][c] = 2
        for r in range(row):
            for c in range(col):
                if board[r][c] == 1:
                    board[r][c] = 0
                elif board[r][c] in [2,3]:
                    board[r][c] = 1
        