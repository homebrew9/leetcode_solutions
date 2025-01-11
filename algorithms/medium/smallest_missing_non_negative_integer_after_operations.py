#
# LarryNY
#
from typing import List
from collections import Counter

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        N = len(nums)

        d = Counter()
        for i in range(N):
            nums[i] %= value
            d[nums[i]] += 1
        print(f'\td = {d}')

        i = 0
        while d[(i % value)] > 0:
            d[i % value] -= 1
            i += 1
        return i

# Main section
for nums, value in [
                      ([1,-10,7,13,6,8], 5),
                      ([1,-10,7,13,6,8], 7),
                   ]:
    print(f'nums, value = {nums}, {value}')
    sol = Solution()
    r = sol.findSmallestInteger(nums, value)
    print(f'r = {r}')
    print('=====================')

