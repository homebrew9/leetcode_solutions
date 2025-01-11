class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hsh1 = dict()
        hsh2 = dict()
        for a, b in zip(s, t):
            if a in hsh1 and hsh1[a] != b:
                    return False
            elif b in hsh2 and hsh2[b] != a:
                    return False
            else:
                hsh1[a] = b
                hsh2[b] = a
        return True

# Main section
sol = Solution()
for s, t in [
               ('egg', 'add'),
               ('foo', 'bar'),
               ('paper', 'title'),
               ('badc', 'baba'),
            ]:
    print(f's = {s} ; t = {t}')
    r = sol.isIsomorphic(s, t)
    print(f'r = {r}')
    print('======================')

