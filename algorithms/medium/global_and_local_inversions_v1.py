from typing import List

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        if nums[0] == 1 and nums[1] == 0:
            print(f'\t{nums[2:]}')
            print(f'\t{sorted(nums[2:])}')
            if nums[2:] == sorted(nums[2:]):
                return True
        return False

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
               [0,1],
               [4,2,0,5,7,10,9,11,8,6,1,3],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.isIdealPermutation(nums)
    print(f'r = {r}')
    print('=================')


