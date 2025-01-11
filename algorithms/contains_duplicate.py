from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hsh = dict()
        for n in nums:
            if n in hsh:
                return True
            else:
                hsh[n] = 1
        return False

# Main section
sol = Solution()
for nums in [
               [1,2,3,1],
               [1,2,3,4],
               [1,1,1,3,3,4,3,2,4,2],
               [2,3,-2,4],
               [-2,0,-1],
               [1,2,-2,1,3,4,-4,-3],
               [1,2,3,0,0,-8,8],
            ]:
    print(f'nums = {nums}')
    r = sol.containsDuplicate(nums)
    print(f'r    = {r}')
    print('===========================')


