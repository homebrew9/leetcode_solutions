from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Pivot on forward diagonal, then reverse all columns
        N = len(matrix)
        lim = N - 1
        for r in range(N):
            col = lim
            row = N - 1
            for c in range(lim):
                #print(f'({r}, {c}) <=> ({row}, {col})')
                matrix[r][c], matrix[row][col] = matrix[row][col], matrix[r][c]
                row -= 1
            lim -= 1
            #print('=====')
        for c in range(N):
            top, bottom = 0, N - 1
            while top < bottom:
                #print(f'({top}, {c}) <=> ({bottom}, {c})')
                matrix[top][c], matrix[bottom][c] = matrix[bottom][c], matrix[top][c]
                top += 1
                bottom -= 1

# Main section
for matrix in [
                 [[1,2],[3,4]],
                 [[1,2,3],[4,5,6],[7,8,9]],
                 [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]],
                 [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],
              ]:
    print(f'matrix = {matrix}')
    sol = Solution()
    sol.rotate(matrix)
    print(f'matrix = {matrix}')
    print('=================')


