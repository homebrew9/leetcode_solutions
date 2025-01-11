from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(rows-1, -1, -1):
            #print(f'Starting point: (r,0) = ({r}, 0)')
            value = matrix[r][0]
            c = 0
            while True:
                nr = r + 1
                nc = c + 1
                if 0 <= nr < rows and 0 <= nc < cols:
                    #print(f'\tChecking (nr, nc) = ({nr}, {nc})')
                    if matrix[nr][nc] != value:
                        return False
                    r, c = nr, nc
                else:
                    break
        for c in range(1, cols):
            #print(f'Starting point: (c, 0) = ({c}, 0)')
            value = matrix[0][c]
            r = 0
            while True:
                nr = r + 1
                nc = c + 1
                if 0 <= nr < rows and 0 <= nc < cols:
                    #print(f'\tChecking (nr, nc) = ({nr}, {nc})')
                    if matrix[nr][nc] != value:
                        return False
                    r, c = nr, nc
                else:
                    break
        return True

# Main section
for matrix in [
                 [[1,2,3,4],[5,1,2,3],[9,5,1,2]],
                 [[1,2],[2,2]],
              ]:
    print(f'matrix = {matrix}')
    sol = Solution()
    r = sol.isToeplitzMatrix(matrix)
    print(f'r = {r}')
    print('================')

