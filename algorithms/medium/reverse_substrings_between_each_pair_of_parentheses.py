class Solution:
    def reverseParentheses(self, s: str) -> str:
        def solve(j):
            res = ''
            while j < N and s[j] != ')':
                if s[j] == '(':
                    j, tmp = solve(j+1)
                    res += tmp
                else:
                    res += s[j]
                j += 1
            return j, res[::-1]
        N = len(s)
        i = 0
        ans = ''
        while i < N:
            if s[i] == '(':
                i, tmp = solve(i+1)
                ans += tmp
            else:
                ans += s[i]
            i += 1
        return ans

# Main section
for s in [
            '(abcd)',
            '(u(love)i)',
            '(ed(et(oc))el)',
            'ab(cd(ef)pq)xy',
            'xy(ab)(cd)(ef)(gh)(ij)(kl)(mn)(op)(qr)(st)(uv)(wx)(yz)(ab)(cd)(ef)(gh)(ij)ab',
            'abcd()',
            '(ab(cd(ef(gh(ij)k)l)m)n)',
            'abcdefghijklmn',
            '()()()(((())))',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.reverseParentheses(s)
    print(f'r = {r}')
    print('===================')

