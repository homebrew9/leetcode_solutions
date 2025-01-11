# ============================================================
# Truth table of a OR B
# a    b   c
# 0 or 0 = 0 => so if c = 1, we need to flip one bit
# 0 or 1 = 1 => so if c = 0, we need to flip one or two bits, or (a | b) + (a & b)
# 1 or 0 = 1 => so if c = 0, we need to flip one or two bits, or (a | b) + (a & b)
# 1 or 1 = 1 => so if c = 0, we need to flip one or two bits, or (a | b) + (a & b)
# Pseudocode:
#     if a or b != c:
#         if c == 0:
#             cnt += 1
#         else:
#             cnt += (a or b) + (a and b)
# ============================================================

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a_str = bin(a).replace('0b','').zfill(32)
        b_str = bin(b).replace('0b','').zfill(32)
        c_str = bin(c).replace('0b','').zfill(32)
        #print(f'\ta_str = {a_str}')
        #print(f'\tb_str = {b_str}')
        #print(f'\tc_str = {c_str}')
        res = 0
        for x, y, z in zip(a_str[::-1], b_str[::-1], c_str[::-1]):
            #print(f'\t\tx, y, z, res = {x}, {y}, {z}, {res}')
            if (int(x) or int(y)) != int(z):
                #print(f'\t\t\tin if x or y != z')
                if int(z) == 1:
                    #print(f'\t\t\tin z == 1')
                    res += 1
                else:
                    #print(f'\t\t\tin z == 0')
                    res += (int(x) or int(y)) + (int(x) and int(y))
                #print(f'\t\t\tres = {res}')
        return res

# Main section
for a, b, c in [
                  (2, 6, 5),
                  (4, 2, 7),
                  (1, 2, 3),
                  (12113, 43435, 3273827),
                  (88373, 7227, 3837874),
               ]:
    print(f'a, b, c = {a}, {b}, {c}')
    sol = Solution()
    r = sol.minFlips(a, b, c)
    print(f'r = {r}')
    print('==================')

