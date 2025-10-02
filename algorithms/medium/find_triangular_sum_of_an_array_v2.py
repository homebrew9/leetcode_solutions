from typing import List

class Solution:
    # Recursive solution
    def triangularSum(self, nums: List[int]) -> int:
        def solve(nums):
            if len(nums) == 1:
                return nums[0]
            return solve([(nums[i] + nums[i+1]) % 10 for i in range(len(nums)-1)])
        return solve(nums)

# Main section
for nums in [
               [0,1,2,3,4],
               [1,2,3,4,5],
               [5],
               [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.triangularSum(nums)
    print(f'r = {r}')
    print('==========================')













