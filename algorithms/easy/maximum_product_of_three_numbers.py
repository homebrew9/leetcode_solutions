#
# DOES NOT WORK FOR TEST CASE # 3
#
from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        nums.sort()
        left, right = 0, len(nums)-1
        arr = list()
        iter = 0
        print('====')
        print(f'nums = {nums}')
        while True:
            iter += 1
            if len(arr) == 3:
                break
            if iter <= 2:
                if abs(nums[left]) > abs(nums[right]):
                    arr.append(nums[left])
                    left += 1
                elif abs(nums[right]) > abs(nums[left]):
                    arr.append(nums[right])
                    right -= 1
                else:
                    arr.append(nums[right])
                    right -= 1
                    left += 1
            else:
                if abs(nums[left]) > abs(nums[right]):
                    if nums[left] < 0:
                        arr.append(nums[right])
                        right -= 1
                    else:
                        arr.append(nums[left])
                        left += 1
                else:
                    arr.append(nums[right])
                    right -= 1
            print(f'\tarr = {arr}')
        return arr[0] * arr[1] * arr[2]

# Main section
for nums in [
               #[1,2,3],
               #[0,1,2],
               [9,0,76,-9,3,37,-99,5],
               #[1,2,3,4,5,6,7],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.maximumProduct(nums)
    print(f'r = {r}')
    print('===========================')


