#
# Doesn't work for the last test case!
#
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        max_val, curr = 0, 0
        includesZero = False
        left, right = 0, 0
        zero_count = 0
        while right < N:
            while right < N and left == right and nums[left] == 0:
                left += 1
                right += 1
                zero_count += 1
            if right >= N:
                break
            if nums[right] == 1:
                right += 1
                curr += 1
            else:
                if not includesZero:
                    includesZero = True
                    curr += 1
                    right += 1
                else:
                    zero_count += 1
                    max_val = max(max_val, curr - 1)
                    left = right
                    curr = 0
                    includesZero = False
        if includesZero or zero_count == 0:
            max_val = max(max_val, curr - 1)
        else:
            max_val = max(max_val, curr)
        return max_val

# Main section
for nums in [
               [1,1,0,1],
               [0,1,1,1,0,1,1,0,1],
               [1,1,1],
               [1,0,0,1,1,1,1,1,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,0,1,1],
               [1,1,1,1,1,1,1],
               [1,1,1,1,1,1,0],
               [0,0,1,1,1,1,1,0,0,1,1,0,1,0],
               [0,0,0,0,0,0,0],
               [0,0,1,1],
               [1,0,1,1,1,1,1,1,0,1,1,1,1,1],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.longestSubarray(nums)
    print(f'r = {r}')
    print('===================')



