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
    def numSub_1(self, s: str) -> int:
        # We can try using the formula for "sum of n"
        MOD = 10**9 + 7
        res = 0
        N = len(s)
        i, j = 0, 0
        in_streak = False
        while j < N:
            if in_streak:
                if s[j] == '0':
                    streak = j - i
                    res += streak * (streak + 1) // 2
                    in_streak = False
            elif s[j] == '1':
                in_streak = True
                i = j
            j += 1
        if in_streak:
            streak = j - i
            res += streak * (streak + 1) // 2
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
    r1 = sol.numSub_1(s)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print('=====================')








