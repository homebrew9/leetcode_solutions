from typing import List
from collections import defaultdict

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Sliding window
        N = len(nums)
        nums.sort()
        res = 0
        left, right = 0, 0
        while right < N:
            while right < N and nums[right] - nums[left] <= 1:
                right += 1
            if nums[right-1] - nums[left] == 1:
                res = max(res, right - left)
            if right >= N:
                break
            while left < N and nums[right] - nums[left] > 1:
                left += 1
        return res
    def findLHS_1(self, nums: List[int]) -> int:
        # Using hashmap/dictionary
        N = len(nums)
        hsh = defaultdict(int)
        for i, v in enumerate(nums):
            hsh[v] += 1
        nums.sort()
        res = 0
        for i in range(1, N):
            if nums[i] - nums[i-1] == 1:
                res = max(res, hsh[nums[i]] + hsh[nums[i-1]])
        return res

# Main section
for nums in [
               [1,3,2,2,5,2,3,7],
               [1,2,3,4],
               [1,1,1,1],
               [1,1,1,1,2],
               [2,2,2,3,3,3,4,4,9],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.findLHS(nums)
    r1 = sol.findLHS_1(nums)
    print(f'r    = {r}')
    print(f'r1   = {r1}')
    print('=======================')












