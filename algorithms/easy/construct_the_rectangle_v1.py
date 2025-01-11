from typing import List

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        p = 1
        q = area//2
        #print(f'(p, q) = ({p}, {q})')
        l, w = area, 1
        while p <= q:
            p += 1
            if area % p == 0:
                q = area // p
                #print(f'\t(p, q, area) = ({p}, {q}, {p*q})')
                l, w = p, q
        return [l, w]

# Main section
for area in [
               4,
               37,
               122122,
               1,
               2,
               3,
               10000000,
               9999889,
               10,
               100,
               1000,
               3742327,
               9999999,
               7919,
            ]:
    sol = Solution()
    print(f'area = {area}')
    r = sol.constructRectangle(area)
    print(f'r = {r}')
    assert area == r[0]*r[1]
    print('==========================')


