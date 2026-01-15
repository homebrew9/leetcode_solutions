class Solution:
    def residuePrefixes(self, s: str) -> int:
        res = 0
        seen = set()
        length = 0
        for ch in s:
            seen.add(ch)
            length += 1
            if len(seen) == length % 3:
                res += 1
        return res

# Main section
for s in [
            'abc',
            'dd',
            'bob',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.residuePrefixes(s)
    print(f'r = {r}')
    print('==========================')






