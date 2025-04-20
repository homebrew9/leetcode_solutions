from typing import List
import bisect

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def get_complement(i, lower, upper):
            left_ind = max(i + 1, bisect.bisect_left(nums, lower))
            right_ind = max(i + 1, bisect.bisect_right(nums, upper))
            return right_ind - left_ind
        nums.sort()
        res = 0
        for i, n in enumerate(nums):
            lower_bound = lower - n
            upper_bound = upper - n
            size = get_complement(i, lower_bound, upper_bound)
            res += size
        return res

# Main section
for nums, lower, upper in [
                             ([0,1,7,4,4,5], 3, 6),
                             ([1,7,9,2,5], 11, 11),
                             ([15,-12,-26,41,-70,-23,88,29,-31,-92,36,82,-68,68,-38,-65,-56,-86,84,11,-40,58,-24,7,99,64,-37,39,-66,-45,-58,-3,91,-65,89,21,61], 135, 279),
                          ]:
    print(f'nums, lower, upper = {nums}, {lower}, {upper}')
    sol = Solution()
    r = sol.countFairPairs(nums, lower, upper)
    print(f'r = {r}')
    print('========================')

