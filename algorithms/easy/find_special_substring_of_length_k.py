from collections import Counter
class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        N = len(s)
        for i in range(N):
            chunk = s[i:i+k]
            if len(chunk) != k:
                continue
            cntr = Counter(chunk)
            if len(cntr) == 1:
                res = True
                ch = s[i]
                if i - 1 >= 0 and s[i - 1] == ch:
                    res = False
                    continue
                if i + k < N and s[i+k] == ch:
                    res = False
                if res == True:
                    return True
        return False

# Main section
for s, k in [
               ('aaabaaa', 3),
               ('abc', 2),
               ('jkjhfgg', 2),
               ('h', 1),
            ]:
    print(f's, k = {s}, {k}')
    sol = Solution()
    r = sol.hasSpecialSubstring(s, k)
    print(f'r = {r}')
    print('==========================')

