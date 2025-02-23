class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            next_s = ''
            for i in range(0, len(s)-1):
                next_s += str((int(s[i]) + int(s[i+1])) % 10)
            s = next_s
        return s[0] == s[1]

# Main section
for s in [
            '3902',
            '34789',
            '5834806624619546953328702144012526742080259867289826520512459998847526757640018773855659063054657398',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.hasSameDigits(s)
    print(f'r = {r}')
    print('===================')

