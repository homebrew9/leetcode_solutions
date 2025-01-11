# =====================================
# https://leetcode.com/problems/partition-equal-subset-sum/discuss/1624939/C%2B%2BPython-5-Simple-Solutions-w-Explanation-or-Optimization-from-Brute-Force-to-DP-to-Bitmask
# Brute Force
# =====================================
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def canPart(nums, i=0, sum1=0, sum2=0):
            print(f'\t>>>{" "*i*4}canPart({i}, {sum1}, {sum2})',end='')
            if i >= len(nums):
                print(f' => ({sum1==sum2})')
                return sum1 == sum2
            print('')
            return canPart(nums, i+1, sum1+nums[i], sum2) or canPart(nums, i+1, sum1, sum2+nums[i])
        return canPart(nums)

# Main section
sol = Solution()
for nums in [
               #[1,5,11,5],
               #[1,2,3,5],
               #[1,5,6,8,9,11],
               #[1],
               #[7],
               #[2,3],
               #[4,4],
               #[1,1,7,1,1,1,1,1,6,1,1,1,1,1,1],
               #[1,3,4,4],
               #[1,1,1,1,1,1,1,1],
               #[2,2,1,1],
               [1,1,2,2],
            ]:
    print(f'nums = {nums}')
    r = sol.canPartition(nums)
    print(f'r    = {r}')
    print('==================================')


