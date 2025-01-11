from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # For a matrix:
        #   90 degree clockwise rotation = reverse on forward diagonal + reverse columns
        #   90 degree anti-clockwise rotation = reverse on forward diagonal + reverse rows
        n = len(matrix)
        # Reverse top right part around the diagonal
        c = n-1
        while c >= 0:
            r1, c1 = 0, c
            r2, c2 = n-c1-1, n-1
            while r1 < r2:
                print(f'\tSwap ({r1}, {c1}) <=> ({r2}, {c2})')
                matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
                r1 += 1
                c1 += 1
                r2 -= 1
                c2 -= 1
            c -= 1
        # Reverse bottom left part around the diagonal
        r, c = 1, 0
        while r < n:
            r1, c1 = r, c
            r2, c2 = n-1, n-r1-1
            while r1 < r2:
               print(f'\t\tSwap ({r1}, {c1}) <=> ({r2}, {c2})')
               matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
               r1 += 1
               c1 += 1
               r2 -= 1
               c2 -= 1
            r += 1
        # Now reverse all column values
        c = 0
        while c < n:
            r1, c1 = 0, c
            r2, c2 = n-1, c
            while r1 < r2:
                print(f'\t\tSwap ({r1}, {c1}) <=> ({r2}, {c2})')
                matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
                r1 += 1
                r2 -= 1
            c += 1

        return matrix

# Main section
for matrix in [
                 [[1,2],[3,4]],
                 [[1,2,3],[4,5,6],[7,8,9]],
                 [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]],
              ]:
    print(f'matrix = {matrix}')
    sol = Solution()
    r = sol.rotate(matrix)
    print(f'r = {r}')
    print('=================')

