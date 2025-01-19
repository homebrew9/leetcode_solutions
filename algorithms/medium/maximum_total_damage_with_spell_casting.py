#
# Explanation by user: never_get_piped
#
from typing import List

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        power.sort()
        dp = []
        preMax = 0
        ans = 0
        dpIdx = 0

        i = 0
        while i < len(power):
            while dpIdx < len(dp) and dp[dpIdx][0] + 2 < power[i]:
                preMax = max(preMax, dp[dpIdx][1])
                dpIdx += 1

            j = i
            cur = 0
            while j < len(power) and power[j] == power[i]:
                cur += power[j]
                j += 1

            ans = max(ans, cur + preMax)
            dp.append((power[i], cur + preMax))
            i = j

        return ans

# Main section
for power in [
               [1,1,3,4],
               [7,1,6,6],
               [7,3,3,2,8,5,3,1,5,1,5,1,4,3,5,5,2,2,7,5,8,4,2,5,4,2,7,7,8,3,9,10,1,5,6,4,10,9,7,8,6,2,2,10,3,4,7,3,10,10,4,2,8,3,4,8,10,2,6,8,5,3,2,5,7,7,5,10,6,3,2,6,7,6,3,8,9,8,5,10,10,7,3,8,6,9,8,5,9,3,4,8,5,5,2,9,1,6,2,5],
               [7,1,6,3],
               [1,1,2,2,3,5,8,8,9],
            ]:
    print(f'power = {power}')
    sol = Solution()
    r = sol.maximumTotalDamage(power)
    print(f'r = {r}')
    print('=====================')


