from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
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
    print(f'r    = {r}')
    print('=======================')













