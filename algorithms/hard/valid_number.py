class Solution:
    def isNumber(self, s: str) -> bool:
        N = len(s)
        dot_count = 0
        e_count = 0
        for i in range(N):
            v = s[i]
            if v not in ('-+.0123456789eE'):
                return False
            if v in '-+':
                if i == 0 and N == 1:
                    return False
            if v in 'eE':
                if i == 0:
                    return False
                e_count += 1
                if e_count > 1:
                    return False
                if i == 1 and not s[i-1].isdigit():
                    return False
                if i > 1 and s[i-1] == '.' and not s[i-2].isdigit():
                    return False
                #if not s[i-1].isdigit():
                #    return False
                if i == N - 1:
                    return False
                if i == N - 2 and not s[i+1].isdigit():
                    return False
                if i == N - 3 and s[i+1] in '-+' and not s[i+2].isdigit():
                    return False
            if i > 0 and s[i-1] not in 'eE' and v in ('-', '+'):
                return False
            if v == '.':
                dot_count += 1
                if dot_count > 1:
                    return False
                if i == 0 and N == 1:
                    return False
                if e_count > 0:
                    return False
                if i == N-1 and not s[i-1].isdigit():
                    return False
        return True

# Main section
for s in [
            '0',
            'e',
            '.',
            '+',
            '-',
            '2',
            '0089',
            '-0.1',
            '+3.14',
            '4.',
            '-.9',
            '2e10',
            '-90E3',
            '3e+7',
            '+6e-1',
            '53.5e93',
            '-123.456e789',
            'abc',
            '1a',
            '1e',
            'e3',
            '99e2.5',
            '--6',
            '-+3',
            '95a54e53',
            '+34.',
            '-3.',
            '-.',
            '-e.',
            'a',
            'e.',
            '-3.5E12',
            '-3.5E1.2',
            '-3.5e1.2',
            '3.4.5',
            '-12e-12',
            '+12e+12',
            '-12e+12',
            '+12e-12',
            '.e1',
            '4e+',
            '46.e3',
            '+E3',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.isNumber(s)
    print(f'r = {r}')
    print('================')


