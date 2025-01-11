from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(i).count('1') for i in range(n+1)]

# Main section
for n in [
            0,
            1,
            2,
            3,
            4,
            5,
            100,
            267,
            7809,
            5314,
            35678,
            100000
         ]:
    sol = Solution()
    print(f'n = {n}')
    r = sol.countBits(n)
    print(f'r = {r}')
    print('=====================')

