from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        curr = 0
        for i in range(N):
            if i == 0 or nums[i] > nums[i-1]:
                curr += nums[i]
            else:
                curr = nums[i]
            res = max(res, curr)
        return res

# Main section
for nums in [
               [10,20,30,5,10,50],
               [10,20,30,40,50],
               [12,17,15,13,10,11,12],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.maxAscendingSum(nums)
    print(f'r = {r}')
    print('======================')

