#
# From L. Rossi book
# The last testcase throws "RecursionError: maximum recursion depth exceeded".
#
from typing import List
from functools import cache
import sys

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def solve(t):
            if not t:
                return []
            if t < 0:
                return None
            optimal_result = None
            for c in coins:
                partial_result = solve(t - c)
                if partial_result is None:
                    continue
                candidate = partial_result + [c]
                if (optimal_result is None or len(candidate) < len(optimal_result)):
                    optimal_result = candidate
            return optimal_result
        res = solve(amount)
        #print(coins, amount, res)
        return len(res) if res is not None else -1

# Main section
sys.setrecursionlimit(1000000000)
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


