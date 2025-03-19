from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        for i in range(0, N - 2):
            if nums[i] == 0:
                res += 1
                nums[i] = 1
                nums[i+1] = 0 if nums[i+1] == 1 else 1
                nums[i+2] = 0 if nums[i+2] == 1 else 1
        if nums.count(0) > 0:
            return -1
        return res

# Main section
for nums in [
               [0,1,1,1,0,0],
               [0,1,1,1],
               [0,0,0,0,0,0,0,0,0],
               [1,1,1,1,1,1,1,1,1],
               [1,0,0,0,1,0,0,0,1],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.minOperations(nums)
    print(f'r  = {r}')
    print('================')

