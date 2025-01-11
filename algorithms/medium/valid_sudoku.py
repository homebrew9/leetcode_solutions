from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkLine(board, r, c, rows, cols):
            #print(f'\t\tr, c, rows, cols = {r}, {c}, {rows}, {cols}')
            hsh = {i: 0 for i in range(1,10)}
            if rows is None:
                for i in range(cols):
                    #print(f'\t\t\ti, (r, c+i) = {i}, ({r}, {c+i})')
                    if board[r][c+i] == '.':
                        continue
                    if hsh[int(board[r][c+i])] == 1:
                        return False
                    hsh[int(board[r][c+i])] = 1
            else:
                for i in range(rows):
                    #print(f'\t\t\ti, (r+i, c) = {i}, ({r+i}, {c})')
                    if board[r+i][c] == '.':
                        continue
                    if hsh[int(board[r+i][c])] == 1:
                        return False
                    hsh[int(board[r+i][c])] = 1
            return True

        def checkBox(board, r, c):
            # Given (r, c) the top-left corner of a box, collect all digits in
            # the box and check if they contain the digits 1-9 without repetition.
            hsh = {i: 0 for i in range(1,10)}
            for i in range(r, r+3):
                for j in range(c, c+3):
                    #print(f'\t... (i,j) = ({i},{j})')
                    if board[i][j] == '.':
                        continue
                    if hsh[int(board[i][j])] == 1:
                        return False
                    hsh[int(board[i][j])] = 1
            return True
        
        rows = len(board)
        cols = rows
        for row in range(rows):
            #print(f'\trow, cols = {row}, {cols}')
            if not checkLine(board, row, 0, None, cols):
                #print(f'\t==>row = {row}')
                return False
        for col in range(cols):
            #print(f'\tcol, rows = {col}, {rows}')
            if not checkLine(board, 0, col, rows, None):
                #print(f'\t==>col = {col}')
                return False
        # Check each sub-box
        for row in range(0, rows, 3):
            for col in range(0, cols, 3):
                #print(row, col)
                if not checkBox(board, row, col):
                    print(f'\t==>checkBox({row}, {col})')
                    return False
        return True

# Main section
for board in [
                [["5","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]],
                [["8","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]],
                [["5","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".","6",".",".","8",".",".","7","9"]],
             ]:
    print(f'board = {board}')
    sol = Solution()
    r = sol.isValidSudoku(board)
    print(f'r = {r}')
    print('=================')

