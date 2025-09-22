from typing import List
from functools import reduce

class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        return reduce(lambda x,y: x|y, [n for n in nums if n % 2 == 0] + [0])

# Main section
for nums in [
               [1,2,3,4,5,6],
               [7,9,11],
               [1,8,16],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.evenNumberBitwiseORs(nums)
    print(f'r = {r}')
    print('===================')

