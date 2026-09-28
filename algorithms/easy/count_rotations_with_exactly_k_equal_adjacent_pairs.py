class Solution:
    def countRotations(self, s: str, k: int) -> int:
        def get_score(t):
            N = len(t)
            cnt = 0
            for i in range(N-1):
                if t[i] == t[i+1]:
                    cnt += 1
            return cnt
        N = len(s)
        res = 0
        for i in range(N):
            cnt = get_score(s[i+1:] + s[:i+1])
            if cnt == k:
                res += 1
        return res

# Main section
for s, k in [
               ('aab', 1),
               ('abca', 0),
               ('ndeffuqsonxlwlgscbvkcijvlitrtzhwjynyfecotfybqugvrzrsofvruhdkekrtlvrqtvykxirstscydhmfrsqpchtlxmyhlvdy', 0),
               ('ndeffuqsonxlwlgscbvkcijvlitrtzhwjynyfecotfybqugvrzrsofvruhdkekrtlvrqtvykxirstscydhmfrsqpchtlxmyhlvdy', 1),
               ('ndeffuqsonxlwlgscbvkcijvlitrtzhwjynyfecotfybqugvrzrsofvruhdkekrtlvrqtvykxirstscydhmfrsqpchtlxmyhlvdy', 2),
            ]:
    print(f's, k = {s}, {k}')
    sol = Solution()
    r = sol.countRotations(s, k)
    print(f'r = {r}')
    print('===================================')
















