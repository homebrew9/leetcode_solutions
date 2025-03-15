from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # If length of s is even, all frequencies must be even
        # If length of s is odd, exactly one frequencey must be odd, the rest must be even
        N = len(s)
        isOddLength = N%2 == 1
        cntr = Counter(s)
        oddFound = False
        for v in cntr.values():
            if v%2 == 1:
                if isOddLength:
                    if oddFound:
                        return False
                    oddFound = True
                else:
                    return False
        return True

# Main section
for s in [
            'code',
            'aab',
            'carerac',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.canPermutePalindrome(s)
    print(f'r = {r}')
    print('======================')

