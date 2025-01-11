from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= 0:
                right = mid - 1
            else:
                left = mid + 1
        # In all cases, left will be on either the first 0
        # or first positive integer
        neg = left
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > 0:
                right = mid - 1
            else:
                left = mid + 1
        # Now in all cases, left will be on the first positive int
        pos = len(nums) - left
        return max(neg, pos)

# Main section
for nums in [
               [-2,-1,-1,1,2,3],
               [-3,-2,-1,0,0,1,2],
               [5,20,66,1314],
               [-7,-6,-5,-4,-3,-2,-1,0,0,0,0,0,0,0,0,0,0,0,1],
               [-7,-6,-5,5,6,7],
               [-7,-6,-5,-4,-3,-2,-1,0],
               [-7,-6,-5,-4,-3,-2,-1],
               [-7,-6,-5,5,6,7,8],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.maximumCount(nums)
    print(f'r = {r}')
    print('=================')

