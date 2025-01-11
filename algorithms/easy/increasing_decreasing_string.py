class Solution:
    def sortString(self, s: str) -> str:
        chars = [0] * 26
        for ch in s:
            chars[ord(ch) - 97] += 1
        res = ''
        while True:
            cnt = 0
            for i in range(26):
                if chars[i] > 0:
                    cnt += 1
                    res += chr(i + 97)
                    chars[i] -= 1
            if cnt == 0:
                break
            cnt = 0
            for i in range(25, -1, -1):
                if chars[i] > 0:
                    cnt += 1
                    res += chr(i + 97)
                    chars[i] -= 1
            if cnt == 0:
                break
        return res

# Main section
for s in [
            'aaaabbbbcccc',
            'rat',
            'aaaaabbcddd',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.sortString(s)
    print(f'r = {r}')
    print('=================')

