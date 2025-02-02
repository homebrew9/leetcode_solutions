from collections import Counter
class Solution:
    def findValidPair(self, s: str) -> str:
        cntr = Counter(s)
        N = len(s)
        for i in range(1, N):
            prev = s[i-1]
            curr = s[i]
            if curr != prev and cntr[curr] == int(curr) and cntr[prev] == int(prev):
                return prev + curr
        return ''

# Main section
for s in [
            '2523533',
            '221',
            '22',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.findValidPair(s)
    print(f'r = {r}')
    print('===================')
