class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        res = 0
        streak = 0
        for ch in s:
            if ch == '0':
                streak = 0
            elif ch == '1':
                streak += 1
                res += streak
        return res % MOD

# Main section
for s in [
            '0110111',
            '101',
            '111111',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.numSub(s)
    print(f'r = {r}')
    print('=====================')














