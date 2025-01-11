# =====================================
# https://leetcode.com/problems/partition-equal-subset-sum/discuss/1624939/C%2B%2BPython-5-Simple-Solutions-w-Explanation-or-Optimization-from-Brute-Force-to-DP-to-Bitmask
# Brute Force - optimized
# =====================================
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def subsetSum(s, i=0):
            print(f'\t>>>{" "*i*4}({s}, {i})',end='')
            if s == 0:
                print('  => (True)')
                return True
            if i >= len(nums) or s < 0:
                print('  => (False)')
                return False
            print('')
            return subsetSum(s - nums[i], i+1) or subsetSum(s, i+1)
        totalSum = sum(nums)
        return totalSum % 2 == 0 and subsetSum(totalSum // 2)

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
               #[1,1,2,2],
               [1,2,3,8],
            ]:
    print(f'nums = {nums}')
    r = sol.canPartition(nums)
    print(f'r    = {r}')
    print('==================================')



