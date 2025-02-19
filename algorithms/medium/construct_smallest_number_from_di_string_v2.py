# Another algorithm that uses a stack. This is very efficient.
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        N = len(pattern)
        res = list()
        stack = list()
        for i in range(N + 1):
            stack.append(i + 1)
            while stack and (i == N or pattern[i] == 'I'):
                res.append(str(stack.pop()))
        return ''.join(res)

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

