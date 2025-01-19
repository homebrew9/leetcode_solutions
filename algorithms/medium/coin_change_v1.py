#
# Official solution
#
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def solve(t):
            if t < 0:
                return -1
            if t == 0:
                return 0
            if t in self.memo:
                return self.memo[t]
            res = float('inf')
            for c in coins:
                count = solve(t - c)
                if count == -1:
                    continue
                res = min(res, 1 + count)
            tmp = -1 if res == float('inf') else res
            self.memo[t] = tmp
            return self.memo[t]
        self.memo = dict()
        res = solve(amount)
        return res

# Main section
for coins, amount in [
                        ([1,2,5], 11),
                        ([2], 3),
                        ([1], 0),
                        ([1,2,4,7,3], 56),
                        ([3,5,7,9,11], 10000),
                     ]:
    print(f'coins, amount = {coins}, {amount}')
    sol = Solution()
    r = sol.coinChange(coins, amount)
    print(f'r = {r}')
    print('==================')


