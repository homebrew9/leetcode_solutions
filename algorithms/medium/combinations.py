from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def combinations(i):
            j = 0
            column[i] = column[i-1]
            while column[i] < n-k+i:
                column [i] = column[i] + 1
                if i < k:
                    combinations(i+1)
                else:
                    #print(f'\tcolumn = {column}')
                    res.append(column[1:k+1])
                    #for j in range(1,k+1):
                    #    print(column[j], end='')
                    #print('')
        res = list()
        column = [-1 for _ in range(20)]
        i = 1
        column[0] = 0
        combinations(i)
        return res

# Main section
for n, k in [
               (4, 2),
               (5, 3),
               (20, 10),
            ]:
    print(f'n, k = {n}, {k}')
    sol = Solution()
    r = sol.combine(n, k)
    print(f'r = {r}')
    print('==================')

