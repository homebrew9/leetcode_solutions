from typing import List

class Solution:
    def sortByAbsoluteValue(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=abs)

    def sortByAbsoluteValue_1(self, nums: List[int]) -> List[int]:
        return [y for x, y in sorted([(abs(n), n) for n in nums])]

    def sortByAbsoluteValue_2(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: abs(x))

# Main section
for nums in [
               [3,-1,-4,1,5],
               [-100,100],
               [5,2,-3,2,1,-1,-6,0,4,2,0,1,-3,0,-6,-3,-6,-7,5,5],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.sortByAbsoluteValue(nums)
    r1 = sol.sortByAbsoluteValue_1(nums)
    r2 = sol.sortByAbsoluteValue_2(nums)
    print(f'r    = {r}')
    print(f'r1   = {r1}')
    print(f'r2   = {r2}')
    print('===================')






