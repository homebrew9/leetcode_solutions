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
    def maxDifference_1(self, s: str) -> int:
        cntr = Counter(s)
        max_odd_freq, min_even_freq = float('-inf'), float('inf')
        for v in cntr.values():
            if v % 2 == 1:
                max_odd_freq = max(max_odd_freq, v)
            else:
                min_even_freq = min(min_even_freq, v)
        return max_odd_freq - min_even_freq
    def maxDifference_2(self, s: str) -> int:
        cntr = Counter(s)
        maxOdd = max([v for v in cntr.values() if v % 2 == 1])
        minEven = min([v for v in cntr.values() if v % 2 == 0])
        return maxOdd - minEven

# Main section
for s in [
            'aaaaabbc',
            'abcabcab',
            'tzt',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.maxDifference(s)
    r1 = sol.maxDifference_1(s)
    r2 = sol.maxDifference_1(s)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print(f'r2 = {r2}')
    print('===================')




