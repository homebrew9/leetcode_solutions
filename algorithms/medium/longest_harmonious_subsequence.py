from collections import defaultdict
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hsh = defaultdict(int)
        res = 0
        for n in nums:
            hsh[n] += 1
        for k, v in hsh.items():
            if k+1 in hsh:
                res = max(res, v + hsh[k+1])
        return res

# Main section
for nums in [
               [1,3,2,2,5,2,3,7],
               [1,2,3,4],
               [1,1,1,1],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.findLHS(nums)
    print(f'r = {r}')
    print('================')

