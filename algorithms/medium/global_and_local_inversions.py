#
# TLE for larger arrays. I think if an array:
#    (a) starts with [1,0] and
#    (b) the rest of the array is sorted, then lconv = gconv
# But there are corner cases for this as well.
#
from typing import List

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        lconv, gconv = 0, 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    #print(f'\tgconv: ({nums[i]}, {nums[j]})')
                    gconv += 1

        #print(f'\t=====')
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                #print(f'\tlconv: ({nums[i]}, {nums[i+1]})')
                lconv += 1

        print(f'lconv, gconv = {gconv}, {lconv}')
        return lconv == gconv

# Main section
for nums in [
               #[1,0,2],
               #[1,2,0],
               #[0,1,2,3,4,5],
               #[5,4,3,2,1,0],
               #[2,1,0,5,4,3],
               #[2,1,0,3,4,5],
               #[3,2,1,0,6,5,4],
               #[3,2,1,0,4,5,6],
               #[1,2,3,0,4,5,6],
               #[1,2,3,0,6,5,4],
               #[3,2,1,0,4,5,6],
               #[3,2,1,0,6,5,4],
               #[0,1,2,3,4,5,6],
               #[0,6,5,4,3,2,1],
               #[6,5,4,3,2,1,0],
               #[1,2,3,4,5,6,0],
               #[0,6,1,5,2,4,3],
               #[1,0,2,3,4,5,6],
               #[1,0,2,3,4,6,5],
               #[1,0,2,3,6,4,5],  # False
               #[1,0,2,6,3,4,5],  # False
               #[1,0,2,3,6,5,4],  # False
               #[1,0,2,6,5,4,3],  # False
               #[1,0,2,4,3,5,6],
               #[1,0,2,4,3,5,6],
               [0,2,1,4,3,6,5,7],
               [4,2,0,5,7,10,9,11,8,6,1,3],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.isIdealPermutation(nums)
    print(f'r = {r}')
    print('=================')

