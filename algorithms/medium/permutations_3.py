from typing import List

class Solution:
    def permute(self, n: int) -> List[List[int]]:
        def solve(arr, parity):
            lst = self.odd if parity == 'odd' else self.even
            lst_perm = self.odd_perm if parity == 'odd' else self.even_perm
            if len(lst) == 0:
                lst_perm.append(arr[:])
                return
            for i in range(len(lst)):
                num = lst.pop(i)
                solve(arr + [num], parity)
                lst.insert(i, num)
        def weave(arr1, arr2):
            ans = list()
            N, M = len(arr1), len(arr2)
            i, j = 0, 0
            while i < N or j < M:
                ans.append(arr1[i])
                i += 1
                if j < M:
                    ans.append(arr2[j])
                    j += 1
            return ans
        self.odd = [x for x in range(1, n + 1, 2)]
        self.even = [x for x in range(2, n + 1, 2)]
        self.odd_perm = list()
        self.even_perm = list()
        solve([], 'odd')
        solve([], 'even')
        res = list()
        for lst_o in self.odd_perm:
            for lst_e in self.even_perm:
                if len(lst_o) >= len(lst_e):
                    res.append(weave(lst_o, lst_e))
        for lst_e in self.even_perm:
            for lst_o in self.odd_perm:
                if len(lst_e) >= len(lst_o):
                    res.append(weave(lst_e, lst_o))
        return sorted(res)

# Main section
for n in [
            1, 2, 3, 4,
            5, 6,
        ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.permute(n)
    print(f'r = {r}')
    print('==================')

