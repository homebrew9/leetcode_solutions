from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # All differences must be divisible by x. Minimum total operations is the
        # sum of differences from the median.
        rows = len(grid)
        cols = len(grid[0])
        nums = list()
        for r in range(rows):
            for c in range(cols):
                nums.append(grid[r][c])
        N = len(nums)
        nums.sort()
        diff = [nums[i] - nums[i-1] for i in range(1, N)]
        if any([d % x != 0 for d in diff]):
            return -1
        mid = nums[N//2]
        res = 0
        for n in nums:
            res += abs(n - mid)//x
        return res

# Main section
for grid, x in [
                  ([[2,4],[6,8]], 2),
                  ([[1,5],[2,3]], 1),
                  ([[1,2],[3,4]], 2),
               ]:
    print(f'grid, x = {grid}, {x}')
    sol = Solution()
    r = sol.minOperations(grid, x)
    print(f'r = {r}')
    print('========================')

