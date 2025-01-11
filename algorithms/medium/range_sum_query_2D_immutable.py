from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # Calculate prefix sum for each row and store the prefix sum matrix
        # as a member variable. In the sumRegion function, simply find the
        # diff between sums for each row.
        rows = len(matrix)
        cols = len(matrix[0])
        self.mat = [[None for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if c == 0:
                    self.mat[r][c] = matrix[r][c]
                else:
                    self.mat[r][c] = self.mat[r][c-1] + matrix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sumRegion = 0
        for r in range(row1, row2+1):
            sumRegion += self.mat[r][col2] - (0 if col1 == 0 else self.mat[r][col1-1])
        return sumRegion

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

obj = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
for params in [
                 [2,1,4,3],
                 [1,1,2,2],
                 [1,2,2,4]
              ]:
    print(f'params = {params}')
    r = obj.sumRegion(*params)
    print(f'r = {r}')
    print('=============')

