#
# A few other techniques to solve the problem.
#
from typing import List
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        # One-liner using functional programming constructs
        return sorted(map(lambda x: x % 2, nums))

    def transformArray_1(self, nums: List[int]) -> List[int]:
        # Using two-pointer approach, and avoiding a sort
        N = len(nums)
        res = [None] * N
        left, right = 0, N - 1
        for i in range(N):
            if nums[i] % 2 == 0:
                res[left] = 0
                left += 1
            else:
                res[right] = 1
                right -= 1
        return res

    def transformArray_2(self, nums: List[int]) -> List[int]:
        # The two-pointer approach can be further simplified, since we only need to
        # keep track of either odd or even elements.
        N = len(nums)
        res = [0] * N
        right = N - 1
        for i in range(N):
            if nums[i] % 2 == 1:
                res[right] = 1
                right -= 1
        return res

# Main section
for nums in [
               [4,3,2,1],
               [1,5,1,4,2],
               [716,129,387,940,873,675,53,687,192,692,669,580,261,52,972,870,277,866,834,551,47,353,653,657,959,458,150,467,297,976],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.transformArray(nums)
    print(f'r    = {r}')
    r1 = sol.transformArray_1(nums)
    print(f'r1   = {r1}')
    r2 = sol.transformArray_2(nums)
    print(f'r2   = {r2}')
    print('================================')

