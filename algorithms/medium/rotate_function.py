from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        N = len(nums)
        res = sum([i * v for i, v in enumerate(nums)])
        curr = res
        total = sum(nums)
        for i in range(N - 1, -1, -1):
            curr += total - nums[i] * N
            res = max(res, curr)
        return res

# Main section
for nums in [
               [4,3,2,6],
               [100],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.maxRotateFunction(nums)
    print(f'r = {r}')
    print('==================================')



