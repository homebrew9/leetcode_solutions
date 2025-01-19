#
# A few things to keep in mind.
# 1) Frequency of x must be even. And frequency of y must be even. Otherwise this cannot be solved.
# 2) Indexes that have the same characters in both strings do not affect the result. They can be ignored.
# 3) 'xx'- 'yy' takes 1 swap to fix. 'xy' - 'yx' takes 2 swaps to fix.
# 4) Count all "x_Y" and "y_x" pairs from both strings.
# 5) If sum of both counts is odd then return -1. We need a pair to make the strings equal.
# 6) Each 2 count of "x_y" needs 1 swap. So add x_y // 2 to the result.
# 7) Each 2 count of "y_x" needs 1 swap. So add y_x // 2 to the result.
# 8) If we still have 1 count of "x_y" and 1 count of "y_x" then they need 2 swaps, so add 2 to the result.
#

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x_y, y_x = 0, 0
        for a, b in zip(s1, s2):
            if a != b:
                if a == 'x':
                    x_y += 1
                else:
                    y_x += 1
        if (x_y + y_x) % 2 == 1:
            return -1
        res = x_y // 2
        res += y_x // 2
        if x_y % 2 == 1:
            res += 2
        return res

# Main section
for s1, s2 in [
                 ('xx', 'yy'),
                 ('xy', 'yx'),
                 ('xx', 'xy'),
                 ('xxxxxyyyyy', 'yyyyxyyyyy'),
                 ('xyyyyxxxyxxxxyyxyyyyxyyxyyyxyxyxyyxyxxyyyyxyyxyxxyyyxxyxxxxxyxyxyyxyxyyxyyyxyxxyxyyxyxyyyyyyyxyxxyxy', 'xxxyxyxyxyyyyyxyyxyxxxyyyyxyyxxyyyyyyyxxyyyyxyxxxyxxxxyyyyxyxyxxyxxxyxxxyyxyyyxyxxyxyxxxxyyyxyyyyxyy'),
                 ('xyyyyxxxyxxxxyyxyy', 'xxxyxyxyxyyyyyyyyx'),
              ]:
    print(f's1, s2 = {s1}, {s2}')
    sol = Solution()
    r = sol.minimumSwap(s1, s2)
    print(f'r = {r}')
    print('====================')


