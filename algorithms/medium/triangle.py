from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        cur_row, next_row = [0]*n, triangle[n-1]        
        for level in range(n-2,-1,-1):
            for i in range(level+1):
                cur_row[i] = triangle[level][i] + min(next_row[i], next_row[i+1])
            cur_row, next_row = next_row, cur_row
        return next_row[0]

# Main section
for triangle in [
                   [[2],[3,4],[6,5,7],[4,1,8,3]],
                ]:
    print(f'triangle = {triangle}')
    sol = Solution()
    r = sol.minimumTotal(triangle)
    print(f'r = {r}')
    print('==================')

