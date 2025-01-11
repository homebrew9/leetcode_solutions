#
# Leetcode solution : good use of "all"
#
from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return all(nums[i] <= nums[i+1] for i in range(len(nums)-1)) or \
               all(nums[i] >= nums[i+1] for i in range(len(nums)-1))

# Main section
for nums in [
               [1,2,2,3],
               [6,5,4,4],
               [1,3,2],
               [1,1,1,1,1,1],
               [1,1,1,1,1,2],
               [5,1,1,1,1,1],
               [7,1,1,1,1,2],
               [0,1,1,1,1,0],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.isMonotonic(nums)
    print(f'r = {r}')
    print('==========================')

