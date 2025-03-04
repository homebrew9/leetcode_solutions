#
# List comprehension is the fastest, 3-array technique is the slowest. Functional approach is somewhere in between.
#
from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        return [x for x in nums if x < pivot] + [x for x in nums if x == pivot] + [x for x in nums if x > pivot]

    def pivotArray_1(self, nums: List[int], pivot: int) -> List[int]:
        arr_pre, arr_eq, arr_post = list(), list(), list()
        for n in nums:
            if n < pivot:
                arr_pre += [n]
            elif n == pivot:
                arr_eq += [n]
            else:
                arr_post += [n]
        return arr_pre + arr_eq + arr_post

# Main section
for nums, pivot in [
                      ([9,12,5,10,14,3,10], 10),
                      ([-3,4,3,2], 2),
                   ]:
    print(f'nums, pivot = {nums}, {pivot}')
    sol = Solution()
    r = sol.pivotArray(nums, pivot)
    print(f'r  = {r}')
    r1 = sol.pivotArray_1(nums, pivot)
    print(f'r1 = {r1}')
    print('=========================')

