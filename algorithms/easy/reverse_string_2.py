class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ''
        n = 0
        chunk = s[:k]
        while chunk != '':
            #print(f'\t(n, chunk) = ({n}, {chunk})')
            if n % 2 == 0:
                res += chunk[::-1]
            else:
                res += chunk
            n += 1
            s = s[k:]
            chunk = s[:k]
        return res

# Main section
for s, k in [
               ('abcdefg', 2),
               ('abcd', 2),
               ('abcdefghijklmnopqrstuvwxyz', 3),
               ('a', 1),
               ('ab', 1),
               ('abcd', 1),
               ('abcde', 1),
               ('abcdefg', 1),
               ('a', 5),
               ('ab', 5),
               ('abcde', 5),
               ('abcdef', 5),
               ('abcdefg', 5),
               ('abcdefgh', 5),
               ('abcdefghi', 5),
               ('abcdefghij', 5),
               ('abcdefghijk', 5),
            ]:
    print(f's = {s}, k = {k}')
    sol = Solution()
    r = sol.reverseStr(s, k)
    print(f'r = {r}')
    print('===========================')

