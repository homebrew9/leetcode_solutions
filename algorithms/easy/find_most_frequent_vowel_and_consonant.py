from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        c = Counter([ch for ch in s if ch not in 'aeiou']).most_common(1)
        v = Counter([ch for ch in s if ch in 'aeiou']).most_common(1)
        return (v[0][1] if v else 0) + (c[0][1] if c else 0)

# Main section
for s in [
            'successes',
            'aeiaeia',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.maxFreqSum(s)
    print(f'r = {r}')
    print('===================')

























