from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # Intuition: The max absolute subarray sum is:
        #     i) Either the max subarray sum
        #    ii) Or the min subarray sum
        # So we use Kadane's algorithm to find (i) and (ii).
        # Let's say they are res1 and res2. We then return
        # max(abs(res1), abs(res2)), which is the answer
        #
        N = len(nums)
        max_subarray_sum = float('-inf')
        curr_sum = 0
        for i in range(N):
            curr_sum = max(curr_sum + nums[i], nums[i])
            max_subarray_sum = max(max_subarray_sum, curr_sum)
        min_subarray_sum = float('inf')
        curr_sum = 0
        for i in range(N):
            curr_sum = min(curr_sum + nums[i], nums[i])
            min_subarray_sum = min(min_subarray_sum, curr_sum)
        return max(abs(max_subarray_sum), abs(min_subarray_sum))

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

