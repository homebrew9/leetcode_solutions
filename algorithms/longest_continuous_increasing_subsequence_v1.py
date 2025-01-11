from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_len = 0
        lptr, rptr = None, None
        for i, v in enumerate(nums):
            if i == 0:
                lptr = i
                rptr = i
            elif v > nums[i-1]:
                rptr = i
            elif v <= nums[i-1]:
                lptr = i
                rptr = i
            max_len = max(max_len, rptr-lptr+1)
        return max_len

# Main section
sol = Solution()
for nums in [
               [1,3,5,4,7],
               [2,2,2,2,2],
               [0],
               [-23,-21,-19,-15,-7,-4,-3,-1,0,1,1,2,3,4,5,6,7,9,13,17,99],
               [-23,-21,-19,-15,-7,-4,-3,-1,0,1,1,1,1,1,1,2,3,4,5,6,7,9,13,17,99],
            ]:
    print(f'nums = {nums}')
    r = sol.findLengthOfLCIS(nums)
    print(f'r    = {r}')
    print('=================================')


