from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        inc_len = 1
        dec_len = 1
        res = 0
        for i in range(1, N):
            if nums[i] > nums[i-1]:
                res = max(res, dec_len)
                dec_len = 1
                inc_len += 1
            elif nums[i] < nums[i-1]:
                res = max(res, inc_len)
                inc_len = 1
                dec_len += 1
            else:
                res = max(res, inc_len, dec_len)
                inc_len, dec_len = 1, 1
        res = max(res, inc_len, dec_len)
        return res

# Main section
for nums in [
               [1,4,3,3,2],
               [3,3,3,3],
               [3,2,1],
               [1],
               [1,5],
               [9,1],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.longestMonotonicSubarray(nums)
    print(f'r = {r}')
    print('===============================')

