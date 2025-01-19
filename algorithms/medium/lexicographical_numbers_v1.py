#
# Iterative and recursive variants of the solution.
# The recursive solution needs the limit to be set.
#
from typing import List

#class Solution:
#    def lexicalOrder(self, n: int) -> List[int]:
#        ans = [1]
#        while len(ans) < n:
#            new = ans[-1] * 10
#            while new > n:
#                new //= 10
#                new += 1
#                while new % 10 == 0:    # deal with case like 199+1=200 when we need to restart from 2.
#                    new //= 10
#            ans.append(new)
#        return ans

class Solution(object):
    def __init__(self):
        import sys
        sys.setrecursionlimit(1000000)
    def lexicalOrder(self, n):
        def solve(i):
            if len(self.res) >= n:
                return
            self.res += [i]
            new = self.res[-1] * 10
            while new > n:
                new //= 10
                new += 1
                while new % 10 == 0:
                    new //= 10
            solve(new)
        self.res = list()
        solve(1)
        return self.res

# Main section
for n in [
                1,
                7,
               10,
               17,
              275,
              297,
             1234,
             3748,
             8989,
            50000,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.lexicalOrder(n)
    print(f'r = {r}')
    print('==================')



