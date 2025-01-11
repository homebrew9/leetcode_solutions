#
# WC-365
#
from typing import List
from math import inf

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        N = len(nums)
        total = sum(nums)
        how_many_whole_arrays, rem = divmod(target, total)
        nums = nums + nums
        left = 0
        res = inf
        curr_sum = 0
        for right in range(2*N):
            curr_sum += nums[right]
            while curr_sum > rem:
                curr_sum -= nums[left]
                left += 1
            if curr_sum == rem:
                res = min(res, right-left+1)
        if res == inf:
            return -1
        return res + how_many_whole_arrays*N

# Main section
for nums, target in [
                       ([1,2,3], 5),
                       ([1,1,1,2,3], 4),
                       ([2,4,6,8], 3),
                       ([1,2,2,2,1,2,1,2,1,2,1], 83),
                       ([1,2,3,7], 31),
                       ([1,2,3,7], 34),
                    ]:
    print(f'nums, target = {nums}, {target}')
    sol = Solution()
    r = sol.minSizeSubarray(nums, target)
    print(f'r = {r}')
    print('=================')


