from typing import List
import math

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Iterate from right and return answer when a duplicate is found.
        N = len(nums)
        seen = set()
        for i in range(N-1, -1, -1):
            if nums[i] in seen:
                return math.ceil((i + 1) / 3)
            seen.add(nums[i])
        return 0
    def minimumOperations_1(self, nums: List[int]) -> int:
        N = len(nums)
        seen = set()
        for i in range(N-1, -1, -1):
            if nums[i] in seen:
                # Avoiding math.ceil
                v = (i + 1) // 3
                return v if (i + 1) % 3 == 0 else v + 1
            seen.add(nums[i])
        return 0


# Main section
for nums in [
               [1,2,3,4,2,3,3,5,7],
               [4,5,6,4,4],
               [6,7,8,9],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.minimumOperations(nums)
    r1 = sol.minimumOperations_1(nums)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print('========================')

