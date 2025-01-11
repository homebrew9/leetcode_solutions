from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res = 0
        j = 0
        for i in range(1, len(nums)-1):
            print(f'\ti, j, nums[i], res = {i}, {j}, {nums[i]}, {res} ; cond1 = {nums[j] < nums[i] and nums[i+1] < nums[i]} ; cond2 = {nums[j] > nums[i] and nums[i+1] > nums[i]}')
            # If current element is a hill or valley, then
            # increment res and set j to current index
            if (nums[j] < nums[i] and nums[i+1] < nums[i]) or \
               (nums[j] > nums[i] and nums[i+1] > nums[i]):
                res += 1
                j = i
        return res

# Main section
for nums in [
               [2,4,1,1,6,5],
               [6,6,5,5,4,1],
               [2,1,1,1,5,2,2,1,2],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.countHillValley(nums)
    print(f'r = {r}')
    print('==========================')

