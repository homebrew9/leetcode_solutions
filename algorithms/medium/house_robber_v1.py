#
# https://leetcode.com/problems/house-robber/solutions/156523/from-good-to-great-how-to-approach-most-of-dp-problems/?envType=study-plan&id=algorithm-i
#
from typing import List

class Solution:
    #def rob(self, nums: List[int]) -> int:
    #    # This is a DP problem.
    #    # The following set of recurrence relations help to determine the max
    #    # amount of money that can be robbed.
    #    #     nums[k] = Money at the kth house
    #    #     loot[0] = nums[0]
    #    #     loot[1] = nums[1]
    #    #     loot[k] = max(loot[k-2] + nums[k], loot[k-1])
    #    # The value at loot[-1] is the max loot.
    #    # Let's try using iteration here.
    #    if len(nums) <= 2:
    #        return max(nums)
    #    loot = [None] * len(nums)
    #    loot[0] = nums[0]
    #    loot[1] = nums[1]
    #    for i in range(2, len(nums)):
    #        loot[i] = max(loot[i-2] + nums[i], loot[i-1])
    #    print(f'\tloot = {loot}')
    #    return loot[-1]

    #def rob(self, nums: List[int]) -> int:
    #    def loot(nums, i):
    #        if i < 0:
    #            return 0
    #        return max(loot(nums, i-2) + nums[i], loot(nums, i-1))
    #    return loot(nums, len(nums) - 1)

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        memo = [None] * (len(nums) + 1)
        memo[0] = 0
        memo[1] = nums[0]
        for i in range(1, len(nums)):
            val = nums[i]
            memo[i+1] = max(memo[i], memo[i-1] + val)
        return memo[-1]

# Main section
for nums in [
               [1,2,3,1],
               [2,7,9,3,1],
               [2,7,9,31,1],
               [1,17,20,3,5,51,28,1,11,15],
               [2,1,1,2],
               [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.rob(nums)
    print(f'r = {r}')
    print('=================')

