#
# Ref: https://leetcode.com/problems/global-and-local-inversions/discuss/113644/C%2B%2BJavaPython-Easy-and-Concise-Solution
# Basic on this idea, I tried to arrange an ideal permutation.
# Then I found that to place number i
# I could only place i at A[i-1], A[i] or A[i+1].
# So it came up to me,
# It will be easier just to check if all A[i] - i equals to -1, 0 or 1.

from typing import List

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        return all(abs(i - v) <= 1 for i, v in enumerate(nums))

# Main section
for nums in [
               [1,0,2],
               [1,2,0],
               [0,1,2,3,4,5],
               [5,4,3,2,1,0],
               [2,1,0,5,4,3],
               [2,1,0,3,4,5],
               [3,2,1,0,6,5,4],
               [3,2,1,0,4,5,6],
               [1,2,3,0,4,5,6],
               [1,2,3,0,6,5,4],
               [3,2,1,0,4,5,6],
               [3,2,1,0,6,5,4],
               [0,1,2,3,4,5,6],
               [0,6,5,4,3,2,1],
               [6,5,4,3,2,1,0],
               [1,2,3,4,5,6,0],
               [0,6,1,5,2,4,3],
               [1,0,2,3,4,5,6],
               [1,0,2,3,4,6,5],
               [1,0,2,3,6,4,5],  # False
               [1,0,2,6,3,4,5],  # False
               [1,0,2,3,6,5,4],  # False
               [1,0,2,6,5,4,3],  # False
               [1,0,2,4,3,5,6],
               [1,0,2,4,3,5,6],
               [0,1],
               [4,2,0,5,7,10,9,11,8,6,1,3],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.isIdealPermutation(nums)
    print(f'r = {r}')
    print('=================')

