from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # TC = O(M*N), SC = O(M+N)
        rows = len(matrix)
        cols = len(matrix[0])
        row_set = set([r for r in range(rows) for c in range(cols) if matrix[r][c] == 0])
        col_set = set([c for r in range(rows) for c in range(cols) if matrix[r][c] == 0])
        for r in range(rows):
            for c in range(cols):
                if r in row_set or c in col_set:
                    matrix[r][c] = 0
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















