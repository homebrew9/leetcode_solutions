from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        size = len(nums)
        while i < size and nums[i] < 0 and k > 0:
            print(f'\t\tinside while...')
            nums[i] = -nums[i]
            k -= 1
            i += 1
            print(f'\t\t==> nums = {nums}')
        print(f'\tnums = {nums}')
        array_sum = sum(nums)
        print(f'\tarray_sum = {array_sum}')
        if k % 2 == 1:
            min_value = min(nums)
            print(f'\t\tmin_value = {min_value}')
            array_sum -= 2 * min_value
        return array_sum

# Main section
for nums, k in [
                  ([4,2,3], 1),
                  ([3,-1,0,2], 3),
                  ([2,-3,-1,5,-4], 2),
                  ([-2,5,0,2,-2], 3),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.largestSumAfterKNegations(nums, k)
    print(f'r = {r}')
    print('===================')

