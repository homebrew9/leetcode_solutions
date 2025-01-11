from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        left = 0
        right = 1
        while right < len(nums):
            if nums[right] == nums[left]:
                right += 1
            else:
                left += 1
                nums[left] = nums[right]
        return left + 1

# Main section
for nums in [
               [1,2,3,4,5,5,6,7,8],
               [0,0,1,1,1,2,2,3,3,4,5,6],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.removeDuplicates(nums)
    print(f'r = {r}')
    print(f'{nums[:r]}')
    print('================')

