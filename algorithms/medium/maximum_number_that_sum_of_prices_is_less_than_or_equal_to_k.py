#
#  This is brute force. Does not work for very large k.
#
class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        if x == 1:
            num = 1
            while True:
                price = num.bit_count()
                k -= price
                #if k == 0:
                #    return num
                if k < 0:
                    return num - 1
                num += 1
        else:
            hsh = {2: [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50],
                   3: [3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51],
                   4: [4,8,12,16,20,24,28,32,36,40,44,48,52],
                   5: [5,10,15,20,25,30,35,40,45,50],
                   6: [6,12,18,24,30,36,42,48,54],
                   7: [7,14,21,28,35,42,49,56],
                   8: [8,16,24,32,40,48,56]
                  }
            num = 1
            res = 0
            while True:
                price = sum([(num >> (y-1)) & 1 for y in hsh[x]])
                res += price
                k -= price
                #print('%8d %30s %4d %6d %6d'%(num, bin(num).replace('0b',''), price, k, res))
                if k < 0:
                    return num - 1
                num += 1

# Main section
for k, x in [
               #(4096,6),
               (3278539330613, 5),
            ]:
    print(f'k, x = {k}, {x}')
    sol = Solution()
    r = sol.findMaximumNumber(k, x)
    print(f'r = {r}')
    print('=============')

