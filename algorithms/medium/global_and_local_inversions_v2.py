#
# Ref: https://leetcode.com/problems/global-and-local-inversions/discuss/113644/C%2B%2BJavaPython-Easy-and-Concise-Solution
#
# All local inversions are global inversions.
# If the number of global inversions is equal to the number of local inversions,
# it means that all global inversions in permutations are local inversions.
# It also means that we can not find A[i] > A[j] with i+2<=j.
# In other words, max(A[i]) < A[i+2]
# In this first solution, I traverse A and keep the current biggest number cmax.
# Then I check the condition cmax < A[i+2]
#

from typing import List

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        cmax = 0
        for i in range(len(nums) - 2):
            cmax = max(cmax, nums[i])
            if cmax > nums[i + 2]:
                return False
        return True

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


