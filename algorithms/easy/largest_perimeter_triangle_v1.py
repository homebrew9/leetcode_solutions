#
# If sequence (a, b, c) is sorted in non-decreasing order, and
# a + b > c, then this is the necessary and sufficient condition
# for a, b, c to form a triangle. This can be proved by
# considering various cases
# (e.g. (a=b=c), (a,a+dx,a+dx), (a,a,a+dx) etc.)
#
from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-3, -1, -1):
            if nums[i] + nums[i+1] > nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0

# Main section
for nums in [
               [2,1,2],
               [1,2,1],
               [1,5,9,6,7,9,18],
               [2,9,6,4,5,3,1,1,1],
               [2,9,4,4,5,3,1,1,1],
               [2,2,1,1,1],
               [2,1,1,1],
               [1,1,1,1],
               [1,1,5,11,29,90],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.largestPerimeter(nums)
    print(f'r = {r}')
    print('=============================')

