from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]
        N = len(nums)
        res = list()
        for i in range(N):
            if i == 0:
                if nums[i] > lower:
                    res.append([lower, nums[i]-1])
            elif nums[i] > nums[i-1] + 1:
                res.append([nums[i-1]+1, nums[i]-1])
        if nums[-1] < upper:
            res.append([nums[-1]+1, upper])
        return res

# Main section
for nums, lower, upper in [
                             ([0,1,3,50,75], 0, 99),
                             ([-1], -1, -1),
                          ]:
    print(f'nums, lower, upper = {nums}, {lower}, {upper}')
    sol = Solution()
    r = sol.findMissingRanges(nums, lower, upper)
    print(f'r = {r}')
    print('==================================')







