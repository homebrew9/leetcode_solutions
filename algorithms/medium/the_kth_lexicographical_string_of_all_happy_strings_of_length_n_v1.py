class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def solve(s):
            if len(s) == n:
                self.cnt += 1
                if self.cnt == k:
                    self.res = s
                return
            for ch in letters:
                if len(s) > 0:
                    if ch != s[-1]:
                        solve(s + ch)
                else:
                    solve(ch)
        letters = 'abc'
        self.cnt = 0
        self.res = ''
        solve('')
        return self.res

# Main section
for n, k in [
                 (1, 3),
                 (1, 4),
                 (3, 9),
                 (1, 1),
                 (1, 100),
                 (9, 87),
                 (10, 73),
            ]:
    print(f'n, k = {n}, {k}')
    sol = Solution()
    r = sol.getHappyString(n, k)
    print(f'r = {r}')
    print('============================')

