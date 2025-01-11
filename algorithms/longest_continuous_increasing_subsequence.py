from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_len = None
        cur_len = None
        for i, v in enumerate(nums):
            if i == 0:
                max_len = 1
                cur_len = 1
            else:
                if v > nums[i-1]:
                    cur_len += 1
                else:
                    cur_len = 1
            max_len = max(max_len, cur_len)
        return max_len

# Main section
sol = Solution()
for nums in [
               [1,3,5,4,7],
               [2,2,2,2,2],
            ]:
    print(f'nums = {nums}')
    r = sol.findLengthOfLCIS(nums)
    print(f'r    = {r}')
    print('=================================')

