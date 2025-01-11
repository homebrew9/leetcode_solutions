'''
         0 = 00000
         1 = 00001
         2 = 00010
         3 = 00011
         4 = 00100
         5 = 00101
         6 = 00110
         7 = 00111
         8 = 01000
         9 = 01001
        10 = 01010
        11 = 01011
        12 = 01100
        13 = 01101
        14 = 01110
        15 = 01111
        16 = 10000
        17 = 10001
        18 = 10010
        19 = 10011
        20 = 10100

For n = 20: sum of 1's at index 1 = (21 //  2) *  1 + max(0, (21 %  2) -  1) = 10
            sum of 1's at index 2 = (21 //  4) *  2 + max(0, (21 %  4) -  2) = 10
            sum of 1's at index 3 = (21 //  8) *  4 + max(0, (21 %  8) -  4) =  9
            sum of 1's at index 4 = (21 // 16) *  8 + max(0, (21 % 16) -  8) =  8
            sum of 1's at index 5 = (21 // 32) * 16 + max(0, (21 % 32) - 16) =  9
            ...
            sum of 1's at index i = ((n+1)//2**i) * (2**(i-1)) + max(0, ((n+1) % 2**i) - (2**(i-1)))
'''
#
#
class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def getPrice(n):
            # i = 2
            # c = 2**i
            # d = 2**(i-1)
            # p, q = divmod(n+1, c)
            # price = p * d + max(0, q - d)
            # print(price)
            # i = 4
            # c = 2**i
            # d = 2**(i-1)
            # p, q = divmod(n+1, c)
            # price = p * d + max(0, q - d)
            # print(price)
            # i = 6
            # c = 2**i
            # d = 2**(i-1)
            # p, q = divmod(n+1, c)
            # price = p * d + max(0, q - d)
            # =================================
            print(f'n = {n}')
            price = 0
            i = x
            c = 2**i
            d = c//2
            p, q = divmod(n + 1, c)
            while True:
                tmp = p * d + max(0, q - d)
                #print(f'\ti, c, d, p, q, tmp, price = {i}, {c}, {d}, {p}, {q}, {tmp}, {price}')
                if tmp == 0:
                    break
                price += tmp
                i += x
                c = 2**i
                d = c//2
                p, q = divmod(n + 1, c)
            print(f'\tprice = {price}')
            return price
        left, right = 0, 10**15 + 1
        while left <= right:
            mid = (left + right) // 2
            tmp = getPrice(mid)
            if tmp <= k:
                left = mid + 1
            else:
                right = mid - 1
        return right

# Main section
for k, x in [
               (9, 1),
               (7, 2),
               (20, 2),
               (4096,6),
               (3278539330613, 5),
            ]:
    print(f'k, x = {k}, {x}')
    sol = Solution()
    r = sol.findMaximumNumber(k, x)
    print(f'r = {r}')
    print('=============')


