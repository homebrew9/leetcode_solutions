#
# I think this is the most intuitive DFS solution. Posted by S. Pochmann.
#
from typing import List

class Solution(object):
    def lexicalOrder(self, n):
        def dfs(i):
            if i <= n:
                self.res += [i]
                for d in range(10):
                    dfs(10 * i + d)
        self.res = list()
        for i in range(1, 10):
            dfs(i)
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




