class Solution:
    def longestCommonPrefix(self, s: str, t: str) -> int:
        N = len(s)
        M = len(t)
        skip = 0
        res = 0
        i, j = 0, 0
        while i < N and j < M:
            if s[i] != t[j]:
                if skip < 1:
                    skip += 1
                    i += 1
                else:
                    return res
            else:
                res += 1
                i += 1
                j += 1
        return res

# Main section
for s, t in [
               ('madxa', 'madam'),
               ('leetcode', 'eetcode'),
               ('one', 'one'),
               ('a', 'b'),
            ]:
    print(f's, t = {s}, {t}')
    sol = Solution()
    r = sol.longestCommonPrefix(s, t)
    print(f'r = {r}')
    print('========================')

