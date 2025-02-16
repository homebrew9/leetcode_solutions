from typing import List

class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        res = 0
        N = len(nums)
        for i in range(N):
            is_good = True
            if i - k >= 0 and nums[i-k] >= nums[i]:
                is_good = False
            if i + k < N and nums[i+k] >= nums[i]:
                is_good = False
            if is_good:
                res += nums[i]
        return res
        
# Main section
for nums, k in [
                  ([1,3,2,1,5,4], 2),
                  ([2,1], 1),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.sumOfGoodNumbers(nums, k)
    print(f'r = {r}')
    print('==========================')

