#
# Prefix Sum
#
from typing import List

class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        N = len(nums)
        # max_left[i] maximum subarray sum from start up to index (i-1)
        max_left = [0 for _ in range(N)]
        for i in range(1, N):
            max_left[i] = max(max_left[i-1] + nums[i-1], 0)
        # max_right[i] = maximum subarray sum from index (i+1) to end
        max_right = [0 for _ in range(N)]
        for i in range(N-2, -1, -1):
            max_right[i] = max(max_right[i+1] + nums[i+1], 0)
        res = float('-inf')
        for i in range(N):
            res = max(res, max_left[i] + max_right[i] + nums[i]*nums[i])
        return res

# Main section
for nums in [
               [2,-1,-4,-3],
               [1,-1,1,1,-1,-1,1],
               [51,-14,-62,79,-23,17,-58,77,38,-22,93,42,72,-85,-39,-78,-49,17,95,70,-36,25,44,65,-37,-25,28,-93,44,72,-97,-56,-48,-41,-88,57,-78,85,50,-10,41,-56,14,-82,78,12,-5,62,-80,13,-28,-91,44,-48,95,71,-40,-18,-64,11,61,42,58,23,-86,-31,-87,11,-84,85,-31,-36,-60,44,88,69,90,54,-28,-23,64,-58,-8,92,32,88,-48,-20,-48,100,-54,-83,73,-42,-87,59,94,38,-21,-36],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.maxSumAfterOperation(nums)
    print(f'r = {r}')
    print('===========================')


