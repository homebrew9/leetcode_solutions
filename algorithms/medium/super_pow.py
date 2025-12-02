from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        res = 1
        for d in b:
            res = ((res**10 % 1337) * (a**d % 1337)) % 1337
        return res

# Main section
for a, b in [
               (2, [3]),
               (2, [1,0]),
               (1, [4,3,3,8,5,2]),
            ]:
    print(f'a, b = {a}, {b}')
    sol = Solution()
    r = sol.superPow(a, b)
    print(f'r = {r}')
    print('===========================')















