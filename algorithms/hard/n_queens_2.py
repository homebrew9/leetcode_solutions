class Solution:
    def totalNQueens(self, n: int) -> int:
        def solve(r, cset, dset, adset):
            print(r, cset, dset, adset)
            if r == n:
                self.res += 1
                return
            for c in range(n):
                pos = (r, c)
                if c not in cset and r - c not in dset and r + c not in adset:
                    cset.add(c)
                    dset.add(r - c)
                    adset.add(r + c)
                    res = solve(r + 1, cset, dset, adset)
                    if not res:
                        cset.remove(c)
                        dset.remove(r - c)
                        adset.remove(r + c)
            return False
        self.res = 0
        cset, dset, adset = set(), set(), set()
        solve(0, cset, dset, adset)
        return self.res

# Main section
for n in [
            #1,
            #2,
            #3,
            4,
            #5,
            #6,
            #7,
            #8,
            #9,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.totalNQueens(n)
    print(f'r = {r}')
    print('=================')


