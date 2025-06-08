from sortedcontainers import SortedList
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
    def clearStars_1(self, s: str) -> str:
        arr = list(s)
        sl = SortedList()
        for i, v in enumerate(arr):
            if v == '*':
                _, ind = sl.pop(0)
                arr[-ind] = '*'
            else:
                sl.add((v, -i))
        return ''.join([ch for ch in arr if ch != '*'])

# Main section
for s in [
            'aaba*',
            'abc',
            'yxzkrclb*foemxxqbzufnajeqaj**yzrzvvfdctdhp***pnavby*osklnzkqdzultlszdgi**tilujoianyehwimvdtip*vbmazsyuqqyl**drcd*',
         ]:
    print(f's  = {s}')
    sol = Solution()
    r = sol.clearStars(s)
    r1 = sol.clearStars_1(s)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print('=============')

