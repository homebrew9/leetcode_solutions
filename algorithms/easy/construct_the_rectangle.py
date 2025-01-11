#
# Very slow solution, especially if the area is a prime number.
# It takes a very long time for area = 9999889 which is the largest prime
# less than 10^7. I think we should only loop until area//2. If no factors
# were found until then no point in going further.
#
from typing import List

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        p = 1
        q = area
        print(f'(p, q) = ({p}, {q})')
        l, w = p, q
        while p <= q:
            p += 1
            if area % p == 0:
                q = area // p
                print(f'\t(p, q, area) = ({p}, {q}, {p*q})')
                l, w = p, q
        return [l, w]

# Main section
for area in [
               #4,
               #37,
               #122122,
               #1,
               #2,
               #3,
               #10000000,
               9999889,
               #10,
               #100,
               #1000,
               #3742327,
               #9999999,
               #7919,
            ]:
    sol = Solution()
    print(f'area = {area}')
    r = sol.constructRectangle(area)
    print(f'r = {r}')
    print('==========================')

