from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            for i in range(len(nums)-1):
                nums[i] = (nums[i] + nums[i+1]) % 10
            nums.pop()
        return nums[0]

# Main section
for nums in [
               [1,2,3,4,5],
               [5],
               [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.triangularSum(nums)
    print(f'r = {r}')
    print('==========================')

