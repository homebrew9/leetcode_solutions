from typing import List
from collections import deque

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        d = deque()
        for n in nums:
            if len(d) == 0:
                d.append(n)
                continue
            if n in d:
                continue
            if n > d[-1]:
                d.append(n)
            elif n < d[0]:
                d.appendleft(n)
            elif n > d[1]:
                d.insert(2,n)
            elif n < d[1]:
                d.insert(1,n)
            if len(d) > 3:
                d.popleft()
        if len(d) < 3:
            return d[-1]
        else:
            return d[0]

# Main section
for nums in [
                 [3,2,1],
                 [1,2],
                 [2,2,3,1],
                 [2,2,3,1,9,7,5],
                 [1,2,3,4,5,6,7,8,9],
                 [9,8,7,6,5,4,3,2,1],
                 [0],
                 [-1,1],
                 [-5,-4,-3,-2,-1],
                 [-1,-2,-3,-4,-5,-5,-5,-5],
                 [2,2,3,3,5,5,4,4,0,-6,0],
                 [2,2,7,7,9,9,4,4,0,-6,0],
            ]:
    sol = Solution()
    print(f'nums = {nums}')
    r = sol.thirdMax(nums)
    print(f'r = {r}')
    print('==========================')

