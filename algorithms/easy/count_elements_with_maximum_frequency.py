from typing import List
from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cntr = Counter(nums)
        return sum([v for _, v in cntr.items() if v == max(cntr.values())])

# Main section
for nums in [
               [1,2,2,3,1,4],
               [1,2,3,4,5],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.maxFrequencyElements(nums)
    print(f'r = {r}')
    print('===================')

