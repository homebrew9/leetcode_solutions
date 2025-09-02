from typing import List
from collections import defaultdict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    rows[row].add(int(board[row][col]))
                    cols[col].add(int(board[row][col]))
                    boxes[(row//3, col//3)].add(int(board[row][col]))
                    
        def backtrack(row, col):
            if row == 8 and col == 9:
                return True
            if col == 9:
                row += 1
                col = 0
            if board[row][col] != '.':
                return backtrack(row, col + 1)
            for num in range(1, 10):
                if num in rows[row] or num in cols[col] or num in boxes[(row//3, col//3)]:
                    continue                    
                rows[row].add(num)
                cols[col].add(num)
                boxes[(row//3, col//3)].add(num)
                board[row][col] = str(num)
                if backtrack(row, col + 1):
                    return True
                rows[row].remove(num)
                cols[col].remove(num)
                boxes[(row//3, col//3)].remove(num)
                board[row][col] = '.'
            return False
        
        backtrack(0, 0)
        print(f'Solved => {board}')

# Main section
for board in [
                [['5','3','.','.','7','.','.','.','.'],['6','.','.','1','9','5','.','.','.'],['.','9','8','.','.','.','.','6','.'],['8','.','.','.','6','.','.','.','3'],['4','.','.','8','.','3','.','.','1'],['7','.','.','.','2','.','.','.','6'],['.','6','.','.','.','.','2','8','.'],['.','.','.','4','1','9','.','.','5'],['.','.','.','.','8','.','.','7','9']],
                [['.','.','.','.','.','.','.','.','.'],['.','9','.','.','1','.','.','3','.'],['.','.','6','.','2','.','7','.','.'],['.','.','.','3','.','4','.','.','.'],['2','1','.','.','.','.','.','9','8'],['.','.','.','.','.','.','.','.','.'],['.','.','2','5','.','6','4','.','.'],['.','8','.','.','.','.','.','1','.'],['.','.','.','.','.','.','.','.','.']],
             ]:
    print(f'board = {board}')
    sol = Solution()
    r = sol.solveSudoku(board)
    print(f'r = {r}')
    print('==========================')

