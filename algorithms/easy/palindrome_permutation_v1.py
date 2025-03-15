class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # Requirement for palindrome: At the most one character can be unmatched.
        # Everything else must be matched.
        seen = set()
        for ch in s:
            if ch in seen:
                seen.remove(ch)
            else:
                seen.add(ch)
        return len(seen) <= 1

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

