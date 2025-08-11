from typing import List

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        powers = list()
        val = 1
        while n > 0:
            bit = n & 1
            if bit == 1:
                powers.append(val)
            val *= 2
            n >>= 1
        pfx = list()
        for i, v in enumerate(powers):
            if i == 0:
                pfx.append(powers[i])
            else:
                pfx.append(pfx[i-1] * powers[i])
        res = list()
        for i, j in queries:
            if i == 0:
                res.append(pfx[j] % MOD)
            else:
                res.append((pfx[j] // pfx[i-1]) % MOD)
        return res

# Main section
for n, queries in [
                     (15, [[0,1],[2,2],[0,3]]),
                     (2, [[0,0]]),
                  ]:
    print(f'n, queries = {n}, {queries}')
    sol = Solution()
    r = sol.productQueries(n, queries)
    print(f'r = {r}')
    print('==========================')






















