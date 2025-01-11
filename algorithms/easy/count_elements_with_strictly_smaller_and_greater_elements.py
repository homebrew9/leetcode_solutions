from typing import List
from collections import Counter

class Solution:
    def countElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        del c[min(c)]
        if len(c) > 0:
            del c[max(c)]
        if len(c) == 0:
            return 0
        return len(list(c.elements()))

# Main section
for nums in [
               [11,7,2,15],
               [-3,3,3,90],
               [3,3,4,4],
               [5,5,5,5,5,5,5],
               [3,3,4,5,6,7,9,9,9],
               [3,3,4,5,6,7,7,9,9,9],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.countElements(nums)
    print(f'r = {r}')
    print('=============================')

