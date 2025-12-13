import math
from typing import List

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7
        first = complexity[0]
        complexity.sort()
        if complexity[0] < first or complexity[1] == first:
            return 0
        N = len(complexity) - 1
        return math.factorial(N) % MOD

# Main section
for complexity in [
                     [1,2,3],
                     [3,3,3,4,4,4],
                     [1,2,3],
                     [3,3,3,4,4,4],
                     [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
                  ]:
    print(f'complexity = {complexity}')
    sol = Solution()
    r = sol.countPermutations(complexity)
    print(f'r = {r}')
    print('===========================')










