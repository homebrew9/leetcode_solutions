from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        cntr = Counter(s)
        odd_freq = [v for v in cntr.values() if v % 2 == 1]
        even_freq = [v for v in cntr.values() if v % 2 == 0]
        res = float('-inf')
        for odd in odd_freq:
            for even in even_freq:
                res = max(res, odd - even)
        return res

# Main section
for s in [
            'aaaaabbc',
            'abcabcab',
            'tzt',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.maxDifference(s)
    print(f'r = {r}')
    print('===================')

