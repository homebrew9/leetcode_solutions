from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)
        freq = [0] * (N*N + 1)
        for r in range(N):
            for c in range(N):
                freq[grid[r][c]] += 1
        for i, v in enumerate(freq):
            if i > 0:
                if v == 2:
                    a = i
                elif v == 0:
                    b = i
        return [a, b]

# Main section
for grid in [
               [[1,3],[2,2]],
               [[9,1,7],[8,9,2],[3,4,6]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.findMissingAndRepeatedValues(grid)
    print(f'r = {r}')
    print('================================')

