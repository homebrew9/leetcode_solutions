class Solution:
    def clearStars(self, s: str) -> str:
        arr = list(s)
        chars = [[] for _ in range(26)]
        for i, v in enumerate(arr):
            if v == '*':
                for j in range(26):
                    if len(chars[j]) > 0:
                        ind = chars[j].pop()
                        arr[ind] = '*'
                        break
            else:
                ind = ord(v) - ord('a')
                chars[ind].append(i)
        return ''.join([ch for ch in arr if ch != '*'])

# Main section
for s in [
            'aaba*',
            'abc',
            'yxzkrclb*foemxxqbzufnajeqaj**yzrzvvfdctdhp***pnavby*osklnzkqdzultlszdgi**tilujoianyehwimvdtip*vbmazsyuqqyl**drcd*',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.clearStars(s)
    print(f'r = {r}')
    print('=============')












