class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = str(n)
        total = 0
        x = ''
        for ch in s:
            if ch != '0':
                x += ch
                total += int(ch)
        if x == '':
            return 0
        return int(x) * total

# Main section
for n in [
            10203004,
            1000,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.sumAndMultiply(n)
    print(f'r = {r}')
    print('===========================')



