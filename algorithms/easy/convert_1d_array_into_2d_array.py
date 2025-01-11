from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        mat = list()
        if len(original) != m * n:
            return mat
        i = 0
        for row in range(m):
            mat.append([item for item in original[i:i+n]])
            i += n
        return mat

# Main section
for original, m, n in [
                         ([1,2,3,4], 2, 2),
                         ([1,2,3], 1, 3),
                         ([1,2], 1, 1),
                         ([1,2,3,4,5,6,7,8], 8, 1),
                         ([1,2,3,4,5,6,7,8], 1, 8),
                      ]:
    print(f'original, m, n = {original}, {m}, {n}')
    sol = Solution()
    r = sol.construct2DArray(original, m, n)
    print(f'r = {r}')
    print('=================')

