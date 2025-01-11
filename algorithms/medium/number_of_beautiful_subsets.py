#
# LarryNY
#
from typing import List
from collections import defaultdict

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        N = len(nums)
        count = 0

        def go(index, current):
            if index == N:
                nonlocal count
                count += 1
                return

            if nums[index] + k not in current and nums[index] - k not in current:
                current[nums[index]] += 1
                go(index + 1, current)
                current[nums[index]] -= 1
                if current[nums[index]] == 0:
                    del current[nums[index]]
            go(index + 1, current)

        go(0, defaultdict(int))
        return count - 1

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

