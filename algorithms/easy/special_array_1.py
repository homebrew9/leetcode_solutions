from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if (nums[i-1] + nums[i]) % 2 == 0:
                return False
        return True

# Main section
for nums in [
               [1],
               [2,1,4],
               [4,3,1,6],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.isArraySpecial(nums)
    print(f'r = {r}')
    print('======================')


