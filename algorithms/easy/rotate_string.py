class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return any([s[i:]+s[:i] == goal for i in range(len(s))])

# Main section
for s, goal in [
                  ('abcde', 'cdeab'),
                  ('abcde', 'abced'),
               ]:
    print(f's, goal = {s}, {goal}')
    sol = Solution()
    r = sol.rotateString(s, goal)
    print(f'r = {r}')
    print('==============================')









