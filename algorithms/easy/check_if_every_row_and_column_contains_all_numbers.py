from typing import List

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            arr = [0 for _ in range(rows+1)]
            for col in range(cols):
                if arr[matrix[row][col]] == 1:
                    return False
                arr[matrix[row][col]] = 1

        for col in range(cols):
            arr = [0 for _ in range(rows+1)]
            for row in range(rows):
                if arr[matrix[row][col]] == 1:
                    return False
                arr[matrix[row][col]] = 1
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

