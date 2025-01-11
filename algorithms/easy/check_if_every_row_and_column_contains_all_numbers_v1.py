#
# Without using extra space. For a given row, iterate through the columns
# and set to negative the column corresponding to current value. For example:
# if row # 2 is [3, 1, 2] then set the value of column 3 to negative, then
# column 1 to negative and then column 2 to negative.
# If the value is already negative, then it has been "visited", hence a duplicate.
# Reverse the signs when iterating through the columns.
#
from typing import List

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for row in range(n):
            for col in range(n):
                pos = abs(matrix[row][col]) - 1
                if matrix[row][pos] < 0:
                    return False
                matrix[row][pos] = -matrix[row][pos]

        #print(f'\tmatrix = {matrix}')
        for col in range(n):
            for row in range(n):
                pos = abs(matrix[row][col]) - 1
                if matrix[pos][col] > 0:
                    return False
                matrix[pos][col] = -matrix[pos][col]
        #print(f'\tmatrix = {matrix}')

        return True

# Main section
for matrix in [
                 [[1,2,3],[3,1,2],[2,3,1]],
                 [[1,1,1],[1,2,3],[1,2,3]],
              ]:
    print(f'matrix = {matrix}')
    sol = Solution()
    r = sol.checkValid(matrix)
    print(f'r = {r}')
    print('=================')


