#
# Sliding window
#
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        ans = N
        newNums = sorted(set(nums))
        j = 0
        for i in range(len(newNums)):
            while j < len(newNums) and newNums[j] < newNums[i] + N:
                j += 1
            count = j - i
            ans = min(ans, N - count)
        return ans

# Main section
for nums in [
               [57,11,29,13,14],
               [4,2,5,3],
               [1,2,3,5,6],
               [1,10,100,1000],
               [1,51,52,53,100],
               [1,51,52,52,53,100],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.minOperations(nums)
    print(f'r = {r}')
    print('======================')

