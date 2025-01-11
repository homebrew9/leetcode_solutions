#
# Just one change required!!! It's very important to understand WHY the
# initial value of min_flips should be s.count('0'). The reason is:
# "This is the number of flips needed when the left window is empty and
# the right window is the whole string." Check the LC solution # 1:
# Dynamic Windows.
#
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        N = len(s)
        min_flips = s.count('0')
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


