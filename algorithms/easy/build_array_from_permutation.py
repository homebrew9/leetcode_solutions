from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [None] * len(nums)
        for i in range(len(ans)):
            ans[i] = nums[nums[i]]
        return ans
    def buildArray_1(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]
    def buildArray_2(self, nums: List[int]) -> List[int]:
        return [nums[i] for i in nums]

# Main section
for nums in [
               [0,2,1,5,3,4],
               [5,0,1,2,3,4],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.buildArray(nums)
    r1 = sol.buildArray_1(nums)
    r2 = sol.buildArray_2(nums)
    print(f'r    = {r}')
    print(f'r1   = {r1}')
    print(f'r2   = {r2}')
    print('============================')

