from typing import List

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, v in enumerate(nums):
            if sum([int(x) for x in str(v)]) == i:
                return i
        return -1

# Main section
for nums in [
               [1,3,2],
               [1,10,11],
               [1,2,3],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.smallestIndex(nums)
    print(f'r    = {r}')
    print('============================')

        