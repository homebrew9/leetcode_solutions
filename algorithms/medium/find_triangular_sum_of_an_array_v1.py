from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        ptr = len(nums) - 1
        while ptr > 0:
            for i in range(ptr):
                nums[i] = (nums[i] + nums[i+1]) % 10
            ptr -= 1
        return nums[0]

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

