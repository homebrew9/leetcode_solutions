from typing import List
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 0
        for n in arr:
            i += 1
            if n == i:
                #print(f'\tin if...')
                continue
            else:
                #print(f'\tin else...')
                while i < n:
                    #print(f'\t\tn, i = {n}, {i}')
                    k -= 1
                    if k == 0:
                        return i
                    i += 1
            #print(f'\tn, i, k = {n}, {i}, {k}')
            #print('=====')

        while k > 0:
            i += 1
            k -= 1
        return i

# Main section
for arr, k in [
                 ([5,6,7,9], 5),
                 ([2,3,4,7,11], 5),
                 ([1,2,3,4], 2),
                 ([1,2,20,21], 5),
                 ([1,2,3,4], 4),
              ]:
    print(f'arr, k = {arr}, {k}')
    sol = Solution()
    r = sol.findKthPositive(arr, k)
    print(f'r = {r}')
    print('=============================')

