class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # Using stack
        stack = list()
        N = len(part)
        arr = list(part)
        for ch in s:
            stack.append(ch)
            if stack[-N:] == arr:
                for _ in range(N):
                    stack.pop()
        return ''.join(stack)

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

