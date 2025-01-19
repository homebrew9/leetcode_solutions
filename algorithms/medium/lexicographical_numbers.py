from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def solve(s):
            #print(s, self.res)
            if int(s) <= n:
                self.res += [int(s)]
            if len(s) < L:
                solve(s + '0')
            elif len(s) == L:
                for i in range(1, 10):
                    tmp = int(s[:-1] + str(i))
                    if tmp <= n:
                        self.res += [tmp]
                    else:
                        break
                new_s = s[:-1].rstrip('9')
                if len(new_s) > 0:
                    next_s = str(int(new_s) + 1)
                    if len(next_s) < L:
                        solve(next_s)
        if n < 10:
            return [i for i in range(1, n+1)]
        L = len(str(n))
        self.res = list()
        solve('1')
        return self.res

# Main section
# I guess the setting below has been implemented in LC. In its absence, the
# script errors out with "maximum recursion" error for any n > 1000.
import sys
sys.setrecursionlimit(1_000_000)

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


