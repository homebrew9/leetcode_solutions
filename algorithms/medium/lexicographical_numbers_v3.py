from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def solve(x):
            self.res.append(x)
            if x * 10 <= n:
                for y in range(10):
                    t = 10 * x + y
                    if t <= n:
                        solve(t)
        self.res = list()
        for i in range(1, 10):
            if i <= n:
                solve(i)
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

