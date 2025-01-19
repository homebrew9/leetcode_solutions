class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        N, M = len(s), len(t)
        i, j = 0, 0
        while j < M:
            # Search for t[j] in s
            found = False
            while i < N:
                if s[i] == t[j]:
                    found = True
                    i += 1
                    break
                i += 1
            # If we have reached the end of string s, then it could
            # be due to two reasons:
            # 1) we found the current character from t and then reached the end of s
            # 2) we could not find the current character from t and reached the end of s
            # We have to distinguish between these two cases.
            # Case 1) s = 'ac', t = 'acting'       => we return len(t) - j - 1
            # Case 2) s = 'clothing', t = 'coding' => we return len(t) - j
            if i >= N:
                return M - j - 1 if found else M - j
            j += 1
        # If we are here, then t is a subsequence of s
        return 0

# Main section
for s, t in [
               ('clothing', 'coding'),
               ('abcd', 'abcd'),
               ('ac', 'acting'),
               ('abcdef', 'bdf'),
               ('coaching', 'coding'),
               ('abcde', 'a'),
               ('z', 'abcde'),
               ('commodity', 'coding'),
               ('commodity', 'cody'),
               ('commodity', 'mot'),
               ('commodity', 'motty'),
               ('a', 'a'),
               ('a', 'z'),
            ]:
    print(f's, t = {s}, {t}')
    sol = Solution()
    r = sol.appendCharacters(s, t)
    print(f'r = {r}')
    print('===================')


