from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_value = float('inf')
        max_diff = float('-inf')
        max_found = False

        for num in nums:
            if num < min_value:
                min_value = num
            if num  != min_value and num - min_value > max_diff:
                max_diff = num - min_value
                max_found = True
        if max_found:
            return max_diff
        else:
            return -1

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

