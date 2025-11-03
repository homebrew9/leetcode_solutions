from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        return [nums[i] for i in range(1, len(nums)) if nums[i] == nums[i-1]]

# Main section
for nums in [
               [0,1,1,0],
               [0,3,2,1,3,2],
               [7,1,5,4,3,4,6,0,9,5,8,2],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.getSneakyNumbers(nums)
    print(f'r = {r}')
    print('=====================')


