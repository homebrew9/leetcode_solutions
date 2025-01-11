from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        if rows == 0:
            return mat
        cols = len(mat[0])
        dist = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        # First pass - check for left and top
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                else:
                    if r > 0:
                        dist[r][c] = min(dist[r][c], dist[r-1][c] + 1)
                    if c > 0:
                        dist[r][c] = min(dist[r][c], dist[r][c-1] + 1)
        print(f'\tdist = {dist}')
        # Second pass - check for bottom and right
        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if r < rows - 1:
                    dist[r][c] = min(dist[r][c], dist[r+1][c] + 1)
                if c < cols - 1:
                    dist[r][c] = min(dist[r][c], dist[r][c+1] + 1)
        print(f'\tdist = {dist}')
        return dist

# Main section
for mat in [
              [[1,1,1],[1,1,1],[0,1,0]],
           ]:
    print(f'mat = {mat}')
    sol = Solution()
    r = sol.updateMatrix(mat)
    print(f'r = {r}')
    print('================')

