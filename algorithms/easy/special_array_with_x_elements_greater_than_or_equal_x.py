from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        # Special case: length is the x
        if len(nums) <= nums[0]:
            return len(nums)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # Calculate x - nos. larger than current value
            x = len(nums) - mid
            if nums[mid] >= x:
                # Make sure no value is >= x on the left side
                if nums[mid-1] < x:
                    return x
                right -= 1
            else:
                left += 1
        return -1

# Main section
for nums in [
               [3,5],
               [0,0],
               [0,4,3,0,4],
               [1,2,3,4,5],
               [1,3,3,4,5],
               [0,0,1,1,1,1,5,5,6,7,9,9,9,10,10,11],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.specialArray(nums)
    print(f'r = {r}')
    print('=================')

