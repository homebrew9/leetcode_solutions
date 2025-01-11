#
# twitch_tv_qiqi_impact
#
from typing import List
from collections import defaultdict

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        ret = -1
        def dfs(idx):
            nonlocal ret
            if idx == len(nums):
                ret += 1
                return
            v = nums[idx]
            if d[v] == 0:
                d[v-k] += 1
                d[v+k] += 1
                dfs(idx+1)
                d[v-k] -= 1
                d[v+k] -= 1
            dfs(idx+1)
        dfs(0)
        return ret

# Main section
for nums, k in [
                  #([2,4,6], 2),
                  #([1], 1),
                  ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 2),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.beautifulSubsets(nums, k)
    print(f'r = {r}')
    print('===================')

