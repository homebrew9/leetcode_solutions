class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res = ''
        s = s.replace('-','').upper()
        while s[-k:]:
            res = '-' + s[-k:] + res
            s = s[:-k]
        res = res.lstrip('-')
        return res

# Main section
for s, k in [
               ('5F3Z-2e-9-w', 4),
               ('2-5g-3-J', 2),
               ('ab-c-def-ghi-jkl-m-n-o-p', 3),
               ('ab-c-def-ghi-jkl-m-n-o-p', 2),
               ('ab-c-def-ghi-jkl-m-n-o-p', 1),
               ('a', 1),
               ('aa', 1),
               ('aaa', 1),
               ('aaaa', 1),
               ('a', 5),
               ('aa', 5),
               ('aaa', 5),
               ('aaaa', 5),
               ('aaaaa', 5),
               ('aaaaaa', 5),
            ]:
    sol = Solution()
    print(f's = {s}, k = {k}')
    r = sol.licenseKeyFormatting(s, k)
    print(f'r = {r}')
    print('==========================')

