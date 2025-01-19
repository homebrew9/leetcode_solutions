class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def combinations(s):
            if len(s) > 1:
                n = len(s)
                if s[n-2] < s[n-1] and pattern[n-2] == 'D':
                    return
                elif s[n-2] > s[n-1] and pattern[n-2] == 'I':
                    return
            if len(s) == N:
                if s < self.res:
                    self.res = s
                return
            for ch in '123456789':
                if ch not in s:
                    combinations(s + ch)
        N = len(pattern) + 1
        self.res = '9'*N
        combinations('')
        return self.res

# Main section
for pattern in [
                  'IIIDIDDD',
                  'DDD',
                  'DDIDIIDD',
                  'IIDDIIDI',
                  'IIIDDIDD',
                  'IDIDIDID',
                  'IDDI',
                  'IDDDI',
                  'DIID',
                  'DID',
                  'DII',
                  'DDIDIIDD',
              ]:
    print(f'pattern = {pattern}')
    sol = Solution()
    r = sol.smallestNumber(pattern)
    print(f'r = {r}')
    print('====================')


