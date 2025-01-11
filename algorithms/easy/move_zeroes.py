from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pos = -1
        zero_count = 0
        found_zero = False
        for i in range(len(nums)):
            if nums[i] == 0:
                if not found_zero:
                    found_zero = True
                    zero_pos = i
                    zero_count += 1
                else:
                    zero_count += 1
            elif found_zero:
                nums[zero_pos] = nums[i]
                zero_pos += 1
            print(f'\ti, nums = {i}, {nums}')

        print('\t----')
        print(f'\tzero_count = {zero_count}')
        ind = -1
        while zero_count > 0:
            nums[ind] = 0
            ind += -1
            zero_count -= 1
            print(f'\tnums = {nums}')
        print(nums)

# Main section
for nums in [
               [0,1,0,3,12],
               [0],
               [0,0,0,1,2,3],
               [1,2,3,0,0,0],
               [1,0,3,0,5,0],
               [0,1,0,3,0,5],
               [0,0,0,0,0,0],
               [0,0,0,0,0,1],
               [0,0,0,0,2,1],
               [1,0,0,0,0,0],
               [1,2,0,0,0,0],
               [1,2,3,4,5,6],
               [1,0,0,0,0,1],
               [0,0,1,1,0,0],
               [0,0,1,0,0,0],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.moveZeroes(nums)
    print(f'r = {r}')
    print('=====================')

