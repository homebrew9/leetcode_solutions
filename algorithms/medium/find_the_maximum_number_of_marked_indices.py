from typing import List

class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        j = N - 1
        cnt = 0
        for i in range(N//2-1, -1, -1):
            if nums[i] * 2 <= nums[j]:
                cnt += 2
                j -= 1
        return cnt

# Main section
for nums in [
               [3,5,2,4],
               [9,2,5,4],
               [7,6,8],
               [3,3,4,5,5,7,7,8,9,9],
               [3,3,4,5,5,6,7,7,8,9,9],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.maxNumOfMarkedIndices(nums)
    print(f'r = {r}')
    print('==============')

