from typing import List
from collections import Counter

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        lst = list(map(lambda x: nums[x]+nums[x+1], range(len(nums)-1)))
        c = Counter(lst)
        return any(v > 1 for v in c.values())

# Main section
for nums in [
               [4,2,4],
               [1,2,3,4,5],
               [0,0,0],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.findSubarrays(nums)
    print(f'r = {r}')
    print('=====================')

