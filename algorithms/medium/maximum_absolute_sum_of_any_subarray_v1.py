#
# Another algorithm that uses Prefix Sum technique to find max absolute sum.
# After calculating the prefix array, we iterate through it, storing the min and
# max values as we go. If the current element is 0 or positive, we calculate the
# delta with min value. Otherwise, we calculate the delta with max value. The
# max of all such deltas is our answer.
#
from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        N = len(nums)
        pfx = nums[:]
        for i in range(1, N):
            pfx[i] += pfx[i-1]
        min_val = 0
        max_val = 0
        res = float('-inf')
        for p in pfx:
            if p >= 0:
                res = max(res, abs(p - min_val))
            elif p < 0:
                res = max(res, abs(p - max_val))
            min_val = min(min_val, p)
            max_val = max(max_val, p)
        return res

# Main section
for nums in [
               [1,-3,2,3,-4],
               [2,-5,1,-4,3,-2],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.maxAbsoluteSum(nums)
    print(f'r = {r}')
    print('===================')

