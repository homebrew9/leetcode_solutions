#
# List comprehension is the fastest, 3-array technique is the slowest. Functional approach is somewhere in between.
#
from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        return [elem for _, _, elem in sorted([(-1 if v < pivot else 1 if v > pivot else 0, i, v) for i, v in enumerate(nums)])]
    
    def pivotArray_1(self, nums: List[int], pivot: int) -> List[int]:
        return [elem for _, _, elem in sorted(map(lambda i: (-1 if nums[i] < pivot else 1 if nums[i] > pivot else 0, i, nums[i]), range(len(nums))))]

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

