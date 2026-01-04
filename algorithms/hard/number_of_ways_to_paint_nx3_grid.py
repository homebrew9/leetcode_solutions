import sys
from functools import cache

class Solution:
    def numOfWays(self, n: int) -> int:
        @cache
        def solve(r, c1, c2, c3):
            if r >= n:
                return 1
            res = 0
            if r == 0:
                for c1 in 'RYG':
                    for c2 in 'RYG'.replace(c1,''):
                        for c3 in 'RYG'.replace(c2,''):
                            res += solve(r + 1, c1, c2, c3)
            else:
                for c4 in 'RYG'.replace(c1, ''):
                    for c5 in 'RYG'.replace(c2,'').replace(c4,''):
                        for c6 in 'RYG'.replace(c3,'').replace(c5,''):
                            res += solve(r + 1, c4, c5, c6)
            return res
        sys.setrecursionlimit(1000000)
        MOD = 10**9 + 7
        ans = solve(0, None, None, None)
        return ans % MOD

# Main section
for n in [
            1,
            10,
            50,
            100,
        ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.numOfWays(n)
    print(f'r = {r}')
    print('========================')










