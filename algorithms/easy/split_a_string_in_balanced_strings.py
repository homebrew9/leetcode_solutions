class Solution:
    def balancedStringSplit(self, s: str) -> int:
        total = 0
        ans = 0
        for i, ch in enumerate(s):
            if ch == 'R':
                total += 1
            elif ch == 'L':
                total -= 1
            if total == 0:
                #print(f'\ti = {i} ; ch = {ch}')
                ans += 1
        return ans

# Main section
for s in [
            'RLRRLLRLRL',
            'RLRRRLLRLL',
            'LLLLRRRR',
            'LRLLRLLRLLRRRRRLLLLRRRLRLLRLRRLRLLRRRLLR',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.balancedStringSplit(s)
    print(f'r = {r}')
    print('===========================')

