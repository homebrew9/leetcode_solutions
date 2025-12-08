from collections import defaultdict
from typing import List

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        hsh = defaultdict(tuple)
        for x, y in points:
            if y not in hsh:
                hsh[y] = (1, 0)
            else:
                hsh[y] = (hsh[y][0] + 1, hsh[y][0] + hsh[y][1])
        arr = [hsh[k][1] for k in hsh if hsh[k][0] > 1]
        N = len(arr)
        pfx = [None] * N
        for i in range(N):
            pfx[i] = arr[i] if i == 0 else pfx[i-1] + arr[i]
        res = 0
        for i in range(1, N):
            res = (res + arr[i] * pfx[i-1]) % MOD
        return res % MOD

# Main section
for points in [
                 [[1,0],[2,0],[3,0],[2,2],[3,2]],
                 [[0,0],[1,0],[0,1],[2,1]],
              ]:
    print(f'points = {points}')
    sol = Solution()
    r = sol.countTrapezoids(points)
    print(f'r = {r}')
    print('===========================')



