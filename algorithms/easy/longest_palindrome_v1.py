from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # A palindrome has one of two patterns:
        #  XXXYYYYYYXXX  => divide into two parts, one reverse of the other
        #  XXXYYYZYYYXXX => divide into two parts + "unique center"
        # Determine the occurrence of each character.
        # For each occurrence, add up the nearest even number.
        # Then, if the sum is even and the current occurrence is odd,
        # it means we can add the "unique center".
        res = 0
        for v in Counter(s).values():
            res += v // 2 * 2
            if res % 2 == 0 and v % 2 == 1:
                res += 1
        return res

# Main section
for s in [
            'abccccdd',
            'a',
            'aaaabbbb',
            'aaaabbbccdef',
            'aa',
            'aab',
            'aabaac',
            'ccc',
            'ababababa',
            'aaabbb',
            'aaaaabbbbbcccccddddd',
         ]:
    sol = Solution()
    print(f's = {s}')
    r = sol.longestPalindrome(s)
    print(f'r = {r}')
    print('=====================')

