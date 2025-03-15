from typing import List
import itertools

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        return sum([x[0] != 0 and x[2] % 2 == 0 for x in set(list(itertools.permutations(digits, 3)))])

# Main section
for digits in [
                 [1,2,3,4],
                 [0,2,2],
                 [6,6,6],
                 [1,3,5],
              ]:
    print(f'digits = {digits}')
    sol = Solution()
    r = sol.totalNumbers(digits)
    print(f'r = {r}')
    print('======================')

