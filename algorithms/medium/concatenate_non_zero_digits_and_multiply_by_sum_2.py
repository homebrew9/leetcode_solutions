from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        MOD = 10**9 + 7
        idx = [0] * (n + 1)    # count non-zero digits prefix
        val = [0] * (n + 1)    # concatenation prefix
        tot = [0] * (n + 1)    # digit sum prefix
        pow10 = [1] * (n + 1)  # powers of 10
        for i in range(1, n+1):
            pow10[i] = (pow10[i-1] * 10) % MOD
        c = 0  # number of non-zero digits so far
        for i in range(n):
            d = ord(s[i]) - ord('0')
            if d != 0:
                c += 1
                val[c] = (val[c-1] * 10 + d) % MOD
                tot[c] = tot[c-1] + d
            idx[i + 1] = c
        #print(f'idx = {idx}')
        #print(f'val = {val}')
        #print(f'tot = {tot}')
        #print(f'pow10 = {pow10}')
        ans = list()
        for l, r in queries:
            a = idx[l]
            b = idx[r+1]
            if a == b:
                ans.append(0)
                continue
            length = b - a
            num = (val[b] - val[a] * pow10[length]) % MOD
            sum_digits = tot[b] - tot[a]
            ans.append((num * sum_digits) % MOD)
        return ans

# Main section
for s, queries in [
                     ('10203004', [[0,7],[1,3],[4,6]]),
                     ('1000', [[0,3],[1,1]]),
                     ('9876543210', [[0,9]]),
                  ]:
    print(f's, queries = {s}, {queries}')
    sol = Solution()
    r = sol.sumAndMultiply(s, queries)
    print(f'r = {r}')
    print('===========================')


