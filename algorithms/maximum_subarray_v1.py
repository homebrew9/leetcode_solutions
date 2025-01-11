from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm
        # If the current (running) sum is less than current element, then discard the current sum
        # and set current element as current sum. Max sum takes up the larger value at each iteration.
        currSum = 0
        maxSum = nums[0]
        for i in range(len(nums)):
            currSum = max(currSum + nums[i], nums[i])
            maxSum = max(currSum, maxSum)
        return maxSum

# Main section
sol = Solution()
for nums in [
                 [-2, 1, -3, 4, -1, 2, 1, -5, 4],
                 [1, 2, 3, 4, 5],
                 [-1, -2, -3, -4, -5],
                 [5, 4, -1, 7, 8],
                 [1, -1, 1, -1, 1, -1],
                 [1, -1],
                 [1],
                 [1, 2, 3, -1, -2, -3],
                 [1, 1, 1, 1, 1, 1, 1],
            ]:
    print(f'nums = {nums}')
    r = sol.maxSubArray(nums)
    print(f'r = {r}')
    print('==========================')


