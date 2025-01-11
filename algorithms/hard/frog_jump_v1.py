from collections import defaultdict
from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        def solve(ind, jmp):
            #print(f'\tind, jmp = {ind}, {jmp}')
            if ind == N-1:
                return True
            if (ind, jmp) in self.memo:
                return self.memo[(ind,jmp)]
            n = stones[ind]
            ret = False
            for j in [jmp-1, jmp, jmp+1]:
                if n+j == n:
                    continue
                if (n+j) not in self.pos:
                    continue
                ret = ret or solve(self.pos[n+j], j)
            self.memo[(ind,jmp)] = ret
            return self.memo[(ind,jmp)]
        N = len(stones)
        self.pos = defaultdict(int)
        self.memo = dict()
        for i, v in enumerate(stones):
            self.pos[v] = i
        # Given: "Initially, the frog is on the first stone and assumes
        # the first jump must be 1 unit." Looks like when the frog is on
        # the first stone, it *has not* made the first jump. And if that first
        # jump is 1 unit, then stones[1] must be 1 more than stones[0].
        if stones[1] != stones[0] + 1:
            return False
        return solve(1, 1)

# Main section
for stones in [
                 [0,1,3,5,6,8,12,17],
                 [0,1,2,3,4,8,9,11],
                 [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,19,20,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,49,50,56,60,65,67,68,71,75,83,95,111,124,132,133,147,164,167,168,169,171,178,184,204,205,211,226,238,246,247,305,312,318,336,338,373,389,404,415,418,421,434,442,460,475,489,491,494,497,517,522,536,538,575,582,601,607,631,653,661,666,669,693,718,720,732,739,746,763,788,793,798,803,806,833,834,837,854,871,872,878,880,889,891,896,901,903,905,935,948,953,966,968,988,995,996,998,999,1000],
                 [0,2],
              ]:
    print(f'stones = {stones}')
    sol = Solution()
    r = sol.canCross(stones)
    print(f'r = {r}')
    print('==================')


