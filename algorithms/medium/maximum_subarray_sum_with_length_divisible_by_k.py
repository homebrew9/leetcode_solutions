from typing import List

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        # Initialize prefix sum array with pfx[0] = 0
        pfx = [0] * (N + 1)
        for i in range(N):
            pfx[i+1] = pfx[i] + nums[i]  # Correct prefix sum
        
        # Track minimum prefix sum for each remainder
        min_pfx = [float('inf')] * k
        min_pfx[0] = 0  # Virtual prefix sum at index -1 (pfx[0] = 0)
        
        res = float('-inf')
        for i in range(1, N + 1):
            rem = i % k  # (i) % k = (index_in_pfx) % k
            # Update result using current prefix and min_pfx[rem]
            res = max(res, pfx[i] - min_pfx[rem])
            # Update min_pfx for this remainder
            min_pfx[rem] = min(min_pfx[rem], pfx[i])
        
        return res # type: ignore

# Main section
for nums, k in [
                  ([1,2], 1),
                  ([-1,-2,-3,-4,-5], 4),
                  ([-5,1,2,-3,4], 2),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.maxSubarraySum(nums, k)
    print(f'r = {r}')
    print('===========================')

