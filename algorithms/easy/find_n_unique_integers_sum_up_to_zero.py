from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        for i in range(1, n//2 + 1):
            arr += [i, -i]
        if n % 2 == 1:
            arr += [0]
        return arr

# Main section
for n in [
            3,
            1,
            20,
            57,
            129,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.sumZero(n)
    print(f'r = {r}')
    print('===================')

