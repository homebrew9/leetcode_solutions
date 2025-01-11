class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        def isValid(s):
            prev = s[0]
            cnt = 0
            valid = True
            for i in range(1, len(s)):
                if s[i] == s[i-1]:
                    cnt += 1
                if cnt >= 2:
                    valid = False
                    break
            return valid
        N = len(s)
        arr = list()
        for i in range(N):
            for j in range(N-1, i-1, -1):
                chunk = s[i:j+1]
                if isValid(chunk):
                    arr.append(len(chunk))
        if len(arr) == 0:
            return 0
        return max(arr)

# Main section
for s in [
            '0010',
            '0001',
            '52233',
            '5494',
            '1111111',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.longestSemiRepetitiveSubstring(s)
    print(f'r = {r}')
    print('==================')

