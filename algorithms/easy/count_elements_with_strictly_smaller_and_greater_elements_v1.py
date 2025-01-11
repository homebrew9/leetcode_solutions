from typing import List

class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i, v in enumerate(nums):
            if i == 0 or i == len(nums)-1:
                continue
            if nums[0] < v and v < nums[len(nums)-1]:
                count += 1
        return count

# Main section
for nums in [
               [11,7,2,15],
               [-3,3,3,90],
               [3,3,4,4],
               [5,5,5,5,5,5,5],
               [3,3,4,5,6,7,9,9,9],
               [3,3,4,5,6,7,7,9,9,9],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.countElements(nums)
    print(f'r = {r}')
    print('=============================')

