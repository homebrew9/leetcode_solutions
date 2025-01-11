from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [None for _ in range(n+1)]
        # Cost of climbing stairs when you're at the end, is 0
        dp[n] = 0
        dp[n-1] = cost[n-1]
        # Update the dp array
        for i in range(n-2, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])

        print(f'\tdp = {dp}')
        return min(dp[0], dp[1])

# Main section
for cost in [
               [1,100,1,1,1,100,1,1,100,1],
               [10,15,20],
            ]:
    print(f'cost = {cost}')
    sol = Solution()
    r = sol.minCostClimbingStairs(cost)
    print(f'r = {r}')
    print('========================')

