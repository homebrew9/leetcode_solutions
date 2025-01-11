from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidSubBox(row, col):
            nums = [0] * (rows + 1)
            for r in range(row, row+3):
                for c in range(col, col+3):
                    #print(f'\t\tr, c = {r}, {c}')
                    n = board[r][c]
                    if n != '.':
                        if nums[int(n)] == 1:
                            return False
                        nums[int(n)] = 1
            return True

        rows = len(board)
        cols = len(board[0])
        nums = None
        # Check rows
        for r in range(rows):
            nums = [0] * (cols + 1)
            for c in range(cols):
                n = board[r][c]
                if n != '.':
                    if nums[int(n)] == 1:
                        return False
                    nums[int(n)] = 1
        # Check cols
        for c in range(cols):
            nums = [0] * (rows + 1)
            for r in range(rows):
                n = board[r][c]
                if n != '.':
                    if nums[int(n)] == 1:
                        return False
                    nums[int(n)] = 1
        # Check sub-boxes
        for r in range(0,rows,3):
            for c in range(0,cols,3):
                #print(f'\tr, c = {r}, {c}')
                ret = isValidSubBox(r, c)
                if not ret:
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

