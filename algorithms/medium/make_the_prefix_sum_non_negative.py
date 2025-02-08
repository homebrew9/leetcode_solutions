import heapq
from collections import deque
from typing import List

class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        dq = deque()
        for n in nums:
            dq.append(n)
        h = list()
        heapq.heapify(h)
        res = 0
        psum = 0
        while dq:
            x = dq.popleft()
            heapq.heappush(h, x)
            psum += x
            if psum < 0:
                y = heapq.heappop(h)
                psum -= y
                dq.append(y)
                res += 1
        return res

# Main section
for nums in [
               [2,3,-5,4],
               [3,-5,-2,6],
               [-5,-3,3,-4,0,3,0,-3,4,5],
               [6,-6,-3,3,1,5,-4,-3,-2,-3,4,-1,4,4,-2,6,0],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.makePrefSumNonNegative(nums)
    print(f'r = {r}')
    print('==========================')

