from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Brute force; check the remainder of the array after each jump of 3 steps.
        N = len(nums)
        for i in range(0, N + 3, 3):
            if len(set(nums[i:])) == len(nums[i:]):
                return i // 3

# Main section
for nums in [
               [1,2,3,4,2,3,3,5,7],
               [4,5,6,4,4],
               [6,7,8,9],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.minimumOperations(nums)
    print(f'r = {r}')
    print('========================')

