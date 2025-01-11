from typing import List

class Solution:
    def toHex(self, num: int) -> str:
        # For negative numbers: two's complement is used. If only 4 bits are
        # used, then unsigned numbers would be: [0000, 1111] = [0, 15] and
        # signed numbers would be: [1000, 0111] = [-8, 7]
        # 1000 = 1*(-2^3) + 0 + 0 + 0 = -8
        # ---------     ----------
        # Unsigned      Signed
        # ---------     ----------
        # 0000 =  0     0000 =  0
        # 0001 =  1     0001 =  1
        # 0010 =  2     0010 =  2
        # 0011 =  3     0011 =  3
        # 0100 =  4     0100 =  4
        # 0101 =  5     0101 =  5
        # 0110 =  6     0110 =  6
        # 0111 =  7     0111 =  7
        # 1000 =  8     1000 = -8
        # 1001 =  9     1001 = -7
        # 1010 = 10     1010 = -6 
        # 1011 = 11     1011 = -5 
        # 1100 = 12     1100 = -4 
        # 1101 = 13     1101 = -3 
        # 1110 = 14     1110 = -2 
        # 1111 = 15     1111 = -1 
        # In this scheme (Two's Complement), bin representation for -2 could
        # be found by two methods:
        # Method A: Bin repr of 2 = 0010 ; flip the bits => 1101 ; add 1 to it => 1110
        # Method B: Same as that for 2^4 - 2 = 14 => 1110
        if num == 0:
            return '0'
        hd = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        res = ''
        if num < 0:
            #num = 2**32 + num
            num = 16**8 + num
        while num > 0:
            res = hd[num % 16] + res
            num //= 16 
        return res

# Main section
for num in [
              26,
              283,
              57005,
              48879,
              9999999,
              2147483647,
              1,
              0,
              -1,
              -283,
              -9999999,
              -2147483648,
           ]:
    sol = Solution()
    print(f'num = {num}')
    r = sol.toHex(num)
    print(f'r = {r}')
    print('=====================')


