#
# This logic is completely wrong! We need a stack to keep track of second greatest
# number!
#
from typing import List

class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        first_greatest = -1
        second_greatest = -1
        for i in range(len(nums)-1, -1, -1):
            temp = nums[i]
            if i == len(nums) - 1 or i == len(nums) - 2:
                nums[i] = -1
            else:
                nums[i] = first_greatest
            if second_greatest < temp:
                first_greatest = second_greatest
                second_greatest = temp
            elif first_greatest < temp:
                first_greatest = temp
            #if temp > first_greatest:
            #    first_greatest = temp
            print(f'\ti, nums[i], fg, sg = {i}, {nums[i]}, {first_greatest}, {second_greatest}')
        return nums

# Main section
for nums in [
               [2,4,0,9,6],
               #[17,18,5,4,6,1],
               #[400],
               #[1,2,3,4,5,6,7],
               #[7,6,5,4,3,2,1],
               #[1,1,1,1,1,1],
               #[23,37,23,37,23,37],
           ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.secondGreaterElement(nums)
    print(f'r = {r}')
    print('===========================')

