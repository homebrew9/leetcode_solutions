class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ''
        for i, v in enumerate(s):
            if i >= 2:
                if v == res[-1] and v == res[-2]:
                    continue
            res += v
        return res

# Main section
for s in [
            'leeetcode',
            'aaabaaaa',
            'aab',
         ]:
    print(f's  = {s}')
    sol = Solution()
    r = sol.makeFancyString(s)
    print(f'r  = {r}')
    print('============================')












