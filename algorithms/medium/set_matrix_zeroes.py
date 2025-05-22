from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # TC = O(M+N), SC = O(1)
        rows = len(matrix)
        cols = len(matrix[0])
        is_first_row_zero, is_first_col_zero = False, False
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    if r == 0:
                        is_first_row_zero = True
                    if c == 0:
                        is_first_col_zero = True
                    matrix[0][c] = matrix[r][0] = 0
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        if is_first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0
        if is_first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0
        print(f'~~~~~~~~>{matrix}')
 
# Main section
for matrix in [
                 [[1,1,1],[1,0,1],[1,1,1]],
                 [[0,1,2,0],[3,4,5,2],[1,3,1,5]],
              ]:
    print(f'matrix = {matrix}')
    sol = Solution()
    r = sol.setZeroes(matrix)
    print(f'r = {r}')
    print('============================')
       









