from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        total = sum([sum(grid[r]) for r in range(rows)])
        curr = 0
        for r in range(rows-1):
            curr += sum(grid[r])
            if curr == total / 2:
                return True
        curr = 0
        for c in range(cols-1):
            curr += sum([grid[r][c] for r in range(rows)])
            if curr == total / 2:
                return True
        return False

# Main section
for grid in [
               [[1,4],[2,3]],
               [[1,3],[2,4]],
               [[1,1,1]] ,
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.canPartitionGrid(grid)
    print(f'r = {r}')
    print('==================================')




