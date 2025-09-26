from typing import List
from functools import cache

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def solve(r, c):
            if r == rows:
                return 0
            return triangle[r][c] + min(solve(r+1, c), solve(r+1, c+1))
        rows = len(triangle)
        res = solve(0, 0)
        return res

# Main section
for triangle in [
                   [[2],[3,4],[6,5,7],[4,1,8,3]],
                   [[-10]],
                ]:
    print(f'triangle = {triangle}')
    sol = Solution()
    r = sol.minimumTotal(triangle)
    print(f'r = {r}')
    print('==================')




















