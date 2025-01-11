from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot = -1
        left_sum = 0
        right_sum = sum(nums)
        for i in range(len(nums)):
            right_sum -= nums[i]
            if i > 0:
                left_sum += nums[i-1]
            #print(f'i, left_sum, right_sum = {i}, {left_sum}, {right_sum}')
            if left_sum == right_sum:
                pivot = i
                break
        return pivot

# Main section
for nums in [
               [1,7,3,6,5,6],
               [1,2,3],
               [2,1,-1],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.pivotIndex(nums)
    print(f'r = {r}')
    print('=========================')

