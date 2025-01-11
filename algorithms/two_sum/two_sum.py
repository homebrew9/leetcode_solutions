# Given an array of integers "num" and an integer "target", return indices of
# two numbers such that they add up to "target". You may assume that each input
# would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen = dict()
        for i in range(n):
            if target - nums[i] in seen:
                return [i, seen[target - nums[i]]]
            else:
                seen[nums[i]] = i

# Main section
sol = Solution()
assert set(sol.twoSum([2,7,11,15], 9)) == set([0,1])
assert set(sol.twoSum([3,2,4], 6)) == set([1,2])
assert set(sol.twoSum([3,3], 6)) == set([0,1])
assert set(sol.twoSum([1,2,3,4,5,6,7], 13)) == set([6,5])

