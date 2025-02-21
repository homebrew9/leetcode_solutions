#
# Recursive backtracking solution.
#
from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def solve(s):
            if len(s) == N:
                return s if s not in num_set else None
            if (res := solve(s + '0')):
                return res
            if (res := solve(s + '1')):
                return res
        N = len(nums[0])
        num_set = set(nums)
        return solve('')

# Main section
for nums in [
               ['01','10'],
               ['00','01'],
               ['111','011','001'],
               ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1111'],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.findDifferentBinaryString(nums)
    print(f'r = {r}')
    print('============================')

