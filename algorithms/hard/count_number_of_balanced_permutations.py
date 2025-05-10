from collections import Counter
from math import comb
from functools import cache

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10**9 + 7
        cnt = Counter(int(ch) for ch in num)
        total = sum(int(ch) for ch in num)
        @cache
        def dfs(i, odd, even, balance):
            if odd == 0 and even == 0 and balance == 0:
                return 1
            if i < 0 or odd < 0 or even < 0 or balance < 0:
                return 0
            res = 0
            for j in range(0, cnt[i] + 1):
                res += comb(odd, j) * comb(even, cnt[i] - j) * dfs(i - 1, odd - j, even - cnt[i] + j, balance - i * j)
            return res % MOD

        if total % 2 == 1:
            return 0

        return dfs(9, len(num) - len(num) // 2, len(num) // 2, total // 2)

# Main section
for num in [
              '123',
              '112',
              '12345',
              '000111122',
              '182900281728196475',
           ]:
    print(f'num = {num}')
    sol = Solution()
    r = sol.countBalancedPermutations(num)
    print(f'r   = {r}')
    print('============================')

