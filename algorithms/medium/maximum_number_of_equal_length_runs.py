from collections import defaultdict

class Solution:
    def maxSameLengthRuns(self, s: str) -> int:
        hsh = defaultdict(int)
        N = len(s)
        i, j = 0, 0
        while j < N:
            if s[i] == s[j]:
                j += 1
            else:
                hsh[j - i] += 1
                i = j
        hsh[j - i] += 1
        return max(hsh.values())

# Main section
for s in [
            'hello',
            'aaabaaa',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.maxSameLengthRuns(s)
    print(f'r = {r}')
    print('===========================')






































