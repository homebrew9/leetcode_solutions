from typing import List
from collections import Counter

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        cntr = Counter(nums)
        return max([k for k, v in cntr.items() if v == 1] + [-1])
    def largestUniqueNumber_1(self, nums: List[int]) -> int:
        cntr = Counter(nums)
        res = -1
        for k, v in cntr.items():
            if v == 1:
                res = max(res, k)
        return res

# Main section
for nums in [
               [5,7,3,9,4,9,8,3,1],
               [9,9,8,8],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.largestUniqueNumber(nums)
    r1 = sol.largestUniqueNumber_1(nums)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print('=================')








