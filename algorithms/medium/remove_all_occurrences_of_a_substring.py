class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # Brute force
        N = len(part)
        while (i := s.find(part)) != -1:
            s = s[:i] + s[i+N:]
        return s

# Main section
for s, part in [
                  ('daabcbaabcbc', 'abc'),
                  ('axxxxyyyyb', 'xy'),
                  ('xyabaabcbccz', 'abc'),
               ]:
    print(f's, part = {s}, {part}')
    sol = Solution()
    r = sol.removeOccurrences(s, part)
    print(f'r = {r}')
    print('=======================')

