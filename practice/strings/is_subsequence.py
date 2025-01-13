class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        N, M = len(s), len(t)
        i, j = 0, 0
        while j < M:
            if i < N and t[j] == s[i]:
                i += 1
            if i >= N:
                return True
            j += 1
        if i < N:
            return False
        else:
            return True

# Main section
for s, t in [
               ('abc', 'ahbgdc'),
               ('axc', 'ahbgdc'),
               ('x', 'a'),
               ('', ''),
               ('a', ''),
               ('', 'a'),
               ('', 'abc'),
               ('abc', ''),
            ]:
    print(f's, t = {s}, {t}')
    sol = Solution()
    r = sol.isSubsequence(s, t)
    print(f'r = {r}')
    print('==================')

