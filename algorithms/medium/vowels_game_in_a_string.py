class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # If vowel_count is odd, Alice can pick the entire string and win.
        # If vowel_count is even, Alice can pick a substring with odd vowels from it,
        # leaving odd vowels in the remaining string. Bob will then have to pick a
        # substring with 0 vowels in it. Then Alice picks the remaining substring and wins.
        # The only time Alice loses is when there are 0 vowels in the string.
        vowels = 'aeiou'
        vowel_count = sum([1 if ch in vowels else 0 for ch in s])
        if vowel_count == 0:
            return False
        return True

# Main section
for s in [
            'leetcoder',
            'bbcd',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.doesAliceWin(s)
    print(f'r = {r}')
    print('===================')





















