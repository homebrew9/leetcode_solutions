#
# Generating subsets with backtracking!
#
from collections import defaultdict
from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def solve(arr, i):
            if i >= N:
                return
            for j in range(i, N):
                arr += [nums[j]]
                self.res.append(arr[:])
                solve(arr, j+1)
                arr.pop()
        N = len(nums)
        self.res = list()
        solve([], 0)
        hsh = defaultdict(int)
        N = len(nums)
        for arr in self.res:
            b = 0
            for n in arr:
                b |= n
            hsh[b] += 1
        return hsh[max(hsh)]

# Main section
for nums in [
               [3,1],
               [2,2,2],
               [3,2,1,5],
               [45,5,28,94,34,92,73,7,67,33],
               [91,47,43,70,9,25,84,79,79,52,32,43,38,64,51,30],
               [933,634,838,551,576,30,827,161,69,808,43,495,761,637,657,448],
               [8833,5006,1254,8946,2386,4141,4077,681,8535,4418,8177,9598,8050,6321,7002,9911],
               [21014,98682,7163,33446,79881,46555,74051,41764,95819,112,60077,3193,17412,4213,77009,83250],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.countMaxOrSubsets(nums)
    print(f'r = {r}')
    print('=================')


