import math
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        cnt = 0
        start = 0
        end = int('1'*high, 2)
        for i in range(start, end+1):
            print(f'i = {i}')
            s = bin(i).replace('0b','')
            print(f's = {s}')
            print(f"\t{s.count('0')/zero}, {math.floor(s.count('0')/zero)}")
            print(f"\t{s.count('1')/one}, {math.floor(s.count('1')/one)}")
            if s.count('0')/zero == math.floor(s.count('0')/zero) and s.count('1')/one == math.floor(s.count('1')/one):
                cnt += 1
                print(f"\t\ts, bin = {s}, {bin(int(s)).replace('0b','')}")
        return cnt % mod

# Main section
for low, high, zero, one in [
                               (3, 3, 1, 1),
                               (2, 3, 1, 2),
                            ]:
    print(f'low, high, zero, one = {low}, {high}, {zero}, {one}')
    sol = Solution()
    r = sol.countGoodStrings(low, high, zero, one)
    print(f'r = {r}')
    print('================')

