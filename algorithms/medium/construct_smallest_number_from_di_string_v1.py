# Since we will use the digits 1..9 only once, we set an iterator that returns these digits once in order.
# If we encounter a "D", we increment the count. Otherwise, if we encounter an "I" or if we have reached
# the end, we set the digit and then traverse back, reducing count and setting digits until count is 0.
# Try it with pen and paper for a few test cases!
import string
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        N = len(pattern)
        arr = [0 for _ in range(N + 1)]
        it = iter(string.digits[1:])
        cnt = 0
        for i in range(N + 1):
            if i == N or pattern[i] == 'I':
                arr[i] = it.__next__()
                j = i - 1
                while cnt > 0:
                    arr[j] = it.__next__()
                    j -= 1
                    cnt -= 1
            else:
                cnt += 1
        return ''.join(arr)

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

