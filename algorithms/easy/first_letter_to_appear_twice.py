class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        res = ''
        for ch in s:
            if ch in seen:
                res = ch
                break
            seen.add(ch)
        return res

# Main section
for s in [
            'abccbaacz',
            'abcdd',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.repeatedCharacter(s)
    print(f'r = {r}')
    print('==========================')







