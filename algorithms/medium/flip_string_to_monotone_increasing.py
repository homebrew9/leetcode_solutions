#
# Doesn't work for last test case. Expected answer = 1, actual answer = 2
#
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        N = len(s)
        min_flips = float('inf')
        ones_on_left, zeros_on_right = 0, s.count('0')
        for ch in s:
            if ch == '1':
                ones_on_left += 1
            else:
                zeros_on_right -= 1
            min_flips = min(min_flips, ones_on_left + zeros_on_right)
            print(f'{ch}, {ones_on_left}, {zeros_on_right}, {min_flips}')
        return min_flips
        
# Main section
for s in [
            #'00110',
            #'010110',
            #'00011000',
            #'00000000',
            #'11111111',
            #'01010101010101',
            #'10101010101010',
            '11011',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.minFlipsMonoIncr(s)
    print(f'r = {r}')
    print('===============')

