from typing import List

class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        res = list()
        place_value = 1
        while n > 0:
            q, r = divmod(n, 10)
            val = r * place_value
            if val != 0:
                res = [val] + res
            place_value *= 10
            n = q
        return res

# Main section
for n in [
            537,
            102,
            6,
            102030405,
            400500,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.decimalRepresentation(n)
    print(f'r = {r}')
    print('==========================')










