#
# Check out the Solution section of Leetcode for this problem.
# Problem # 287 - Find the Duplicate Number (Medium)
# Very good overview of 7 different techniques.
#
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            pos = abs(n) - 1
            if nums[pos] < 0:
                return abs(n)
            nums[pos] = -nums[pos]

# Main section
for nums in [
               [1,3,4,2,2],
               [3,1,3,4,2],
               [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,8],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.findDuplicate(nums)
    print(f'r = {r}')
    print('=================')

