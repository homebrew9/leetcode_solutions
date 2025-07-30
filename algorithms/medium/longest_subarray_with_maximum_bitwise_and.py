from typing import List
from collections import defaultdict

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        res = 0
        streak = 0
        for n in nums:
            if n == max_val:
                streak += 1
            else:
                streak = 0
            res = max(res, streak)
        return res
    def longestSubarray_1(self, nums: List[int]) -> int:
        N = len(nums)
        hsh = defaultdict(int)
        i, j = 0, 0
        while j < N:
            if nums[j] != nums[i]:
                hsh[nums[i]] = max(hsh[nums[i]], j - i)
                i = j
            j += 1
        hsh[nums[i]] = max(hsh[nums[i]], j - i)
        return hsh[max(nums)]

# Main section
for nums in [
               [1,2,3,3,2,2],
               [1,2,3,4],
               [1,2,3,3,2,2,2,2,2,3,3,3,1],
               [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
               [5,5,5,5,5,5,5,4,5,5,5,5,5,5,5,5],
               [4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.longestSubarray(nums)
    r1 = sol.longestSubarray_1(nums)
    print(f'r    = {r}')
    print(f'r1   = {r1}')
    print('=================')

