from typing import List
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [None] * len(nums)
        for i in range(len(ans)):
            ans[i] = nums[nums[i]]
        return ans


# Main section
for nums in [
               [0,2,1,5,3,4],
               [5,0,1,2,3,4],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.buildArray(nums)
    print(f'r    = {r}')
    print('========================')


