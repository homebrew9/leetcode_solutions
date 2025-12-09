from sortedcontainers import SortedList
from typing import List

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mod = 10**9 + 7
        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)
        cnt = SortedList()

        dp[0] = 1
        prefix[0] = 1

        j = 0
        for i in range(n):
            cnt.add(nums[i])
            # adjust window
            while j <= i and cnt[-1] - cnt[0] > k: # type: ignore
                cnt.remove(nums[j])
                j += 1
            dp[i + 1] = (prefix[i] - (prefix[j - 1] if j > 0 else 0)) % mod
            prefix[i + 1] = (prefix[i] + dp[i + 1]) % mod

        return dp[n]

# Main section
for nums, k in [
                  ([9,4,1,3,7], 4),
                  ([3,3,4], 0),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.countPartitions(nums, k)
    print(f'r = {r}')
    print('===========================')






