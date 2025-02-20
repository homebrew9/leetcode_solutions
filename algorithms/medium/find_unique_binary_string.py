from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        N = len(nums[0])
        num_set = set([int(n, 2) for n in nums])
        for i in range(0, int('1'*N, 2) + 1):
            if i not in num_set:
                return bin(i).replace('0b', '').zfill(N)

# Main section
for nums in [
               ['01','10'],
               ['00','01'],
               ['111','011','001'],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.findDifferentBinaryString(nums)
    print(f'r = {r}')
    print('============================')

