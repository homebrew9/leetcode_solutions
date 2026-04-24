from typing import List
from math import inf

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        n = len(coins[0])
        dp = [[-inf] * 3 for _ in range(n + 1)]

        dp[1] = [0] * 3
        for row in coins:
            for j, x in enumerate(row):
                dp[j + 1][2] = max(
                    dp[j][2] + x, dp[j + 1][2] + x, dp[j][1], dp[j + 1][1]
                )
                dp[j + 1][1] = max(
                    dp[j][1] + x, dp[j + 1][1] + x, dp[j][0], dp[j + 1][0]
                )
                dp[j + 1][0] = max(dp[j][0], dp[j + 1][0]) + x

        return dp[n][2] # type: ignore

# Main section
for coins in [
                [[0,1,-1],[1,-2,3],[2,-3,4]],
                [[10,10,10],[10,10,10]],
             ]:
    print(f'coins = {coins}')
    sol = Solution()
    r = sol.maximumAmount(coins)
    print(f'r = {r}')
    print('==================================')






