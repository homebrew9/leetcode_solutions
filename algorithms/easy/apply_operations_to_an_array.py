from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        N = len(nums)
        for i in range(N - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        i = 0
        for j in range(N):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
        while i < N:
            nums[i] = 0
            i += 1
        return nums

# Main section
for nums in [
               [1,2,2,1,1,0],
               [0,1],
               [5,2,8,6,7,10,9,2,8,9,7,1,5,8,8,3,9,8,7,8,9,3,3,3,6,0,2,6,8,8],
               [6,4,7,7,10,0,9,4,7,1,2,1,8,0,6,0,6,0,0,4,2,4,4,5,10,7,7,4,5,6,6,8,3,6,1,1,0,2,8,6,9,7,9,0,10,10,5,2,5,4],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.applyOperations(nums)
    print(f'r = {r}')
    print('========================')

