#
# The single element is either the mid point or is in one of the left and right subarrays.
# Let's say the mid point has its partner on its left. Does the single number lie on left
# or right? That depends on the size of left/right subarrays after the mid and its partner
# are removed! So we first determine if the left/right subarrays are odd or even. Then we
# check if they remain odd/even after the mid and its partner is removed. The side that 
# remains odd is the one with the single number.
#
from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        left, right = 0, N - 1
        while left < right:
            mid = (left + right) // 2
            halves_are_even = (right - mid) % 2 == 0
            if nums[mid-1] == nums[mid]:
                if halves_are_even:
                    right = mid - 2
                else:
                    left = mid + 1
            elif nums[mid+1] == nums[mid]:
                if halves_are_even:
                    left = mid + 2
                else:
                    right = mid - 1
            else:
                return nums[mid]
        return nums[left]

# Main section
for nums in [
               [1,1,2,3,3,4,4,8,8],
               [3,3,7,7,10,11,11],
               [1,1,3,3,4,4,8,8,9,9,10],
               [3],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.singleNonDuplicate(nums)
    print(f'r = {r}')
    print('==================')


