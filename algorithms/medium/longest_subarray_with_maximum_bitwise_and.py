from typing import List

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
    print(f'r    = {r}')
    print('=================')







