from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        insertIndex = 1
        for i in range(1, size):
            # Found unique element
            if nums[i-1] != nums[i]:
                # Updating insertIndex in our main array
                nums[insertIndex] = nums[i]
                # Incrementing insertIndex count by 1
                insertIndex += 1
        return insertIndex

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


