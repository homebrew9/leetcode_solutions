from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

# Main section
for nums in [
               [1,2,1],
               [1,3,2,1],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.getConcatenation(nums)
    print(f'r    = {r}')
    print('===========================')

