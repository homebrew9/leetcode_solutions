from typing import List

class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        N = len(nums)
        i = N - 1
        while i >= 1 and nums[i-1] < nums[i]:
            i -= 1
        return i

# Main section
for nums in [
               [1,-1,2,3,3,4,5],
               [4,3,-2,-5],
               [1,2,3,4],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.minimumPrefixLength(nums)
    print(f'r = {r}')
    print('==========================')






