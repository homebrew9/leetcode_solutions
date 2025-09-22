from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return 0 if len(set(nums)) == 1 else 1

# Main section
for nums in [
               [1,2],
               [5,5,5],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.minOperations(nums)
    print(f'r = {r}')
    print('===================')



