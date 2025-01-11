# Check the Solutions tab of leetcode.
# Things to remember:
# 1) n & 1 returns the Least Significant Bit (LSB or rightmost bit) of n
#    This should be easy to prove.
# 2) n >> 1 discards the LSB and shifts all other bits to the right by 1 place.
#    It is the same as dividing n by 2. This is integer division, so decimal
#    places are lost. E.g. 12>>1 = 6 and 7>>1 = 3
# 3) In the right-shift operation, if no bits remain after shifting right, or
#    if there are no bits to shift right, then the answer is 0.
#    E.g. Let's say n = 101 (in binary). Then:
#        n = n >> 1 => n = 10 (in binary)
#        n = n >> 1 => n =  1 (in binary)
#        n = n >> 1 => n =  0 (in binary)
#        n = n >> 1 => n =  0 (in binary)
# ============================================================
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        cnt = 0
        while a or b or c:
            if (c & 1) == 1:
                # If LSB(c) is 1, then flip LSB(a) or LSB(b)
                # only if they both are zeros
                cnt += 0 if (a & 1) or (b & 1) else 1
            else:
                # If LSB(c) is 0, then we need 0, 1 or 2 flips. That can
                # be derived as: LSB(a) + LSB(b)
                cnt += (a & 1) + (b & 1)
            a = a >> 1
            b = b >> 1
            c = c >> 1
        return cnt

# Main section
for a, b, c in [
                  (2, 6, 5),
                  (4, 2, 7),
                  (1, 2, 3),
                  (4, 54, 33),
                  (12113, 43435, 3273827),
                  (88373, 7227, 3837874),
               ]:
    print(f'a, b, c = {a}, {b}, {c}')
    sol = Solution()
    r = sol.minFlips(a, b, c)
    print(f'r = {r}')
    print('==================')


