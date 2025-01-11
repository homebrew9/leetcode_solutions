from typing import List

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        N = len(nums)
        # Start from second last element as the last one is always sorted
        for i in range(N-2, -1, -1):
            # No need to break if already in order
            if nums[i] <= nums[i+1]:
                continue
            # Count how many elements are made from breaking nums[i]
            num_elements = (nums[i] + nums[i+1] - 1)//nums[i+1]
            # It requires num_elements-1 replacement operations
            ans += num_elements - 1
            # Maximize nums[i] after replacement
            nums[i] = nums[i] // num_elements
        return ans

# Main section
for nums in [
               [2,7,9,5,8,8],
               [1,2,3,7,9,5,6],
               [3,9,3],
               [1,2,3,4,5],
               [82,62,38,8,65,83,68,68,91,58],
               [82,62,38],
               [3,29,28],
               [3,60,28],
               [100,82,100,49],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.minimumReplacement(nums)
    print(f'r = {r}')
    print('======================')


