from collections import Counter
from typing import List

class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        res, s1, s2 = [-1] * len(nums), [], []
        for i, a in enumerate(nums):
            while s2 and nums[s2[-1]] < a:
                res[s2.pop()] = a
            tmp = []
            while s1 and nums[s1[-1]] < a:
                tmp.append(s1.pop())
            s2 += tmp[::-1]
            s1.append(i)
        return res

# Main section
for nums in [
               [2,4,0,9,6],
               [3,3],
               [17,18,5,4,6,1],
               [400],
               [1,2,3,4,5,6,7],
               [7,6,5,4,3,2,1],
               [1,1,1,1,1,1],
               [23,37,23,37,23,37],
           ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.secondGreaterElement(nums)
    print(f'r = {r}')
    print('===========================')

