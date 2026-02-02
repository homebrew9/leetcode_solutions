from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # TC = O(N), SC = O(N). No sorting.
        res = nums[0]
        first, second = 10**20, 10**20
        for n in nums[1:]:
            if n < first:
                second = first
                first = n
            elif n < second:
                second = n
        return res + first + second

# Main section
for nums in [
               [1,2,3,12],
               [5,4,3],
               [10,3,1,1],
               [37,14,2,1,21,34,2,26,5,35,2,12,28,48,1,12,1,30,18,13,43,24,27,40,31,6,2,33,50,12,31,5,19,45,47,18,40,42,49,15,8,24,44,20,38,41,26,26,37,9],
               [13,13,13,11,11,11,9],
               [7,7,7],
               [7,8,9],
               [7,7,5],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.minimumCost(nums)
    print(f'r = {r}')
    print('==========================')























