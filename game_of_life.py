## game of life
## https://leetcode.com/problems/game-of-life/
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        copy = [[board[m][n] for n in range(cols)] for m in range(rows)]

        ## define neibor

        neibor_idx = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]

        ## loop over each cell, check neibor and make update
        for m in range(rows):
            for n in range(cols):

                live_neibors = 0

                for i in neibor_idx:
                    row_idx = m + i[0]
                    col_idx = n + i[1]

                    if row_idx>= 0 and col_idx >= 0 and row_idx < rows and col_idx < cols:
                        if copy[row_idx][col_idx] == 1:
                            live_neibors += 1

                if copy[m][n] == 0 and live_neibors == 3:
                    board[m][n] = 1
                elif copy[m][n] == 1:
                    if live_neibors < 2 or live_neibors > 3:
                        board[m][n] = 0
