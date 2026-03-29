from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(mat):
            N = len(mat)
            grid = [[-1 for _ in range(N)] for _ in range(N)]
            for r in range(N):
                row = 0
                col = N - r - 1
                for c in range(N):
                    grid[row][col] = mat[r][c]
                    row += 1
            return grid
        
        if mat == target:
            return True
        for _ in range(3):
            mat = rotate(mat)
            if mat == target:
                return True
        return False

# Main section
for mat, target in [
                      ([[0,1],[1,0]], [[1,0],[0,1]]),
                      ([[0,1],[1,1]], [[1,0],[0,1]]),
                      ([[0,0,0],[0,1,0],[1,1,1]], [[1,1,1],[0,1,0],[0,0,0]]),
                   ]:
    print(f'mat, target = {mat}, {target}')
    sol = Solution()
    r = sol.findRotation(mat, target)
    print(f'r = {r}')
    print('===============================')




