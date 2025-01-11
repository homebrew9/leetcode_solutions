#
# Can we use map to accomplish this task?
#
from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums

# Main section
for nums in [
               [1,2,3,4],
               [1,1,1,1,1],
               [3,1,2,10,1],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.runningSum(nums)
    print(f'r = {r}')
    print('=========================')

