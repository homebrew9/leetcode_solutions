from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_val = float('inf')
        max_diff = -1
        for n in nums:
            if n < min_val:
                min_val = n
            elif n > min_val:
                max_diff = max(max_diff, n - min_val)
        return max_diff

# Main section
for nums in [
               [7,1,5,4],
               [9,4,3,2],
               [1,5,2,10],
               [1,1,1,1],
               [1,2,3,9],
               [9,3,2,1],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.maximumDifference(nums)
    print(f'r = {r}')
    print('===========================')






















