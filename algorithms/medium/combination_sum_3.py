from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def solve(arr, i):
            print(f'arr, i = {arr}, {i}')
            if len(arr) == k:
                if sum(arr) == n:
                    res.append(arr)
                return
            if i > 9:
                return
            for j in range(i, 10):
                if sum(arr) + j <= n:
                    solve(arr + [j], j + 1)
        res = list()
        solve([], 1)
        return res

# Main section
for k, n in [
               (3, 19),
            ]:
    print(f'k, n = {k}, {n}')
    sol = Solution()
    r = sol.combinationSum3(k, n)
    print(f'r = {r}')
    print('================')

