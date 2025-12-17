from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        N = len(prices)
        res = 1
        streak = 1
        for i in range(1, N):
            if prices[i-1] - prices[i] == 1:
                streak += 1
            else:
                streak = 1
            res += streak
        return res

# Main section
for prices in [
                 [3,2,1,4],
                 [8,6,7,7],
                 [1],
              ]:
    print(f'prices = {prices}')
    sol = Solution()
    r = sol.getDescentPeriods(prices)
    print(f'r = {r}')
    print('===========================')










