from collections import defaultdict

class Solution:
    def robotWithString(self, s: str) -> str:
        N = len(s)
        hsh = defaultdict(int)
        for ch in s:
            hsh[ch] += 1
        stack = list()
        res = ''
        for ch in s:
            stack.append(ch)
            hsh[ch] -= 1
            if hsh[ch] == 0:
                del hsh[ch]
            while stack and (len(hsh) == 0 or stack[-1] <= min(hsh)):
                res += stack.pop()
        return res

# Main section
for s in [
            'zza',
            'bac',
            'bdda',
            'bydizfve',
            'bzeyxf',
            'vzhofnpo',
            'mmuqezwmomeplrtskz',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.robotWithString(s)
    print(f'r = {r}')
    print('=============')














