# =======================================================================================================================
#  This can be solved using Dynamic Programming.
#  Let F(i, t) be the probability of coin at index i, and all indexes after it, returning t Heads.
#  Now consider F(0, target) i.e. "probability of coin at index 0 and all indexes after it returning target Heads."
#  Case A) If the first coin returns Head, then we need (target - 1) Heads from the remaining coins. The
#          probability of that event is P1 = F(1, target-1)*prob[0]
#  Case B) If the first coin returns Tail, then we need target Heads from the remaining coins. The
#          probability of that event is P2 = F(1, target)*(1 - prob[0])
#  Thus, total probability is P1 + P2 i.e. F(0, target) = F(1, target-1)*prob[0] + F(1, target)*(1 - prob[0])
#  The recursive relationship is as follows:
#      F(i, t) = F(i+1, t-1)*prob[i] + F(i+1, t)*(1 - prob[i])
#  Termination cases:
#  Case 1) If t < 0, then it means the target has been met. Return 0
#  Case 2) If i == N, then check the value of t.
#          If t = 0, the target has been met, hence return 1 (because we have to multiply it with the probability).
#          If t != 0, the target has not been met, we cannot meet the target now because we are at N, return 0.
# =======================================================================================================================

from typing import List
from functools import cache

class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        @cache
        def solve(i, t):
            if t < 0:
                return 0
            if i == N:
                if t == 0:
                    return 1
                else:
                    return 0
            return solve(i+1, t-1) * prob[i] + solve(i+1, t) * (1 - prob[i])
        N = len(prob)
        res = solve(0, target)
        return res

# Main section
for prob, target in [
                       ([0.5,0.5,0.5,0.5,0.5], 0),
                       ([0.5,0.5,0.5,0.5,0.5], 1),
                       ([0.5,0.5,0.5,0.5,0.5], 2),
                       ([0.5,0.5,0.5,0.5,0.5], 3),
                       ([0.5,0.5,0.5,0.5,0.5], 4),
                       ([0.5,0.5,0.5,0.5,0.5], 5),
                       ([0.5,0.5,0.5,0.5,0.5,0.5], 0),
                       ([0.5,0.5,0.5,0.5,0.5,0.5], 1),
                       ([0.5,0.5,0.5,0.5,0.5,0.5], 2),
                       ([0.5,0.5,0.5,0.5,0.5,0.5], 3),
                       ([0.5,0.5,0.5,0.5,0.5,0.5], 4),
                       ([0.5,0.5,0.5,0.5,0.5,0.5], 5),
                       ([0.5,0.5,0.5,0.5,0.5,0.5], 6),
                    ]:
    print(f'prob, target = {prob}, {target}')
    sol = Solution()
    r = sol.probabilityOfHeads(prob, target)
    print(f'r = {r}')
    print('======================')


