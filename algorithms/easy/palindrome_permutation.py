from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # Requirement for palindrome: there should be 0 or 1 character with odd frequency.
        # There can be 0, 1 or more characters with *even* frequencies - it doesn't matter.
        # But only 1 or less characters with odd frequency.
        return Counter(['E' if v % 2 == 0 else 'O' for v in Counter(s).values()])['O'] <= 1

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

