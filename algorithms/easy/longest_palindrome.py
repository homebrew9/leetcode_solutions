#
# This logic does not work!!
#
from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Determine the occurrence count of each character.
        # Order the characters by their descending occurrence counts
        # Capture even numbers until we reach 1 (if present), add those.
        # A palindrome can be of form: 2n+1 or 2n.
        # Handle the corner case first: a string with only one distinct
        # character occuring any number of times is a palindrome.
        if len(set(s)) == 1:
            return len(s)
        # Now we have a string with more than one distinct character in it.
        cntr = Counter(s)
        h = dict(cntr)
        res = 0
        for k in sorted(h, key=lambda x: h[x], reverse=True):
            if h[k] > 1:
                if h[k] % 2 == 1:
                    res += h[k] - 1
                else:
                    res += h[k]
            else:
                res += h[k]
                break
        return res

# Main section
for s in [
            #'abccccdd',
            #'a',
            #'aaaabbbb',
            #'aaaabbbccdef',
            #'aa',
            #'aab',
            #'aabaac',
            #'ccc',
            'ababababa',
            'aaabbb',
            'aaaaabbbbbcccccddddd',
         ]:
    sol = Solution()
    print(f's = {s}')
    r = sol.longestPalindrome(s)
    print(f'r = {r}')
    print('=====================')

#even, even => aaaabbbb => aabbbbaa => len(s)
#even, odd  => aaaabbb  => aabbbaa  => len(s)
#odd, even  => aaabbbb  => bbaaabb  => len(s)
#odd, odd   => aaabbb   => ababa  a => len(s) - 1


