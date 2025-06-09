from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def solve(i):
            if i <= n:
                res.append(i)
            if 10 * i <= n:
                solve(10 * i)
            if i + 1 <= n and i % 10 < 9:
                solve(i + 1)
        res = list()
        solve(1)
        return res

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







