from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        curr_length, prev_length = 1, 0
        res = 0
        for i in range(1, N):
            if nums[i] > nums[i-1]:
                curr_length += 1
            else:
                prev_length, curr_length = curr_length, 1
            res = max(res, curr_length//2, min(curr_length, prev_length))
        return res

# Main section
for nums in [
               [2,5,7,8,9,2,3,4,3,1],
               [1,2,3,4,4,4,4,5,6,7],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.maxIncreasingSubarrays(nums)
    print(f'r = {r}')
    print('=====================')























