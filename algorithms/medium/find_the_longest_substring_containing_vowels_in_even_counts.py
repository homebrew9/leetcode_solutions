#
# Sliding window. Make sure the approach is very clear! The editorial has a BitMask solution!
#
from collections import Counter

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        N = len(s)
        vowels = 'aeiou'
        for i in range(N, -1, -1):
            for j in range(0, N-i+1):
                chunk = s[j:j+i]
                print('i, j, [j:j+i], chunk = %2d, %2d, [%2d:%2d], [%s%s%s]'%(i, j, j, j+i, ' '*len(s[:j]), chunk, ' '*len(s[j+i:])))
                cntr = Counter(chunk)
                valid = True
                for k, v in cntr.items():
                    if k in vowels and v % 2 == 1:
                        valid = False
                        break
                if valid:
                    return i
        return 0

# Main section
for s in [
            'eleetminicoworoep',
            'leetcodeisgreat',
            'bcbcbc',
            'abcdefghi',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.findTheLongestSubstring(s)
    print(f'r = {r}')
    print('=====================')


