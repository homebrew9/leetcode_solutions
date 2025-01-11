from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        nums.sort()
        # Only two possibilities remain now.
        # nums[0]  * nums[1]  * nums[-1] or
        # nums[-1] * nums[-2] * nums[-3]
        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])

# Main section
for nums in [
               [1,2,3],
               [0,1,2],
               [9,0,76,-9,3,37,-99,5],
               [1,2,3,4,5,6,7],
               [-9,-9,0,3,5,9,37,76],
               [-10,-8,-6,6,8,10],
               [-9,-8,-7,4,5,6],
               [-10,-9,-8,1,2,3],
               [-9,-8,-7,-6],
               [-9,-8,2,3],
               [-9,-7,-5,-3,0,1,4,6,7],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.maximumProduct(nums)
    print(f'r = {r}')
    print('===========================')



