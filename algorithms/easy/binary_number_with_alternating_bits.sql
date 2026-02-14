class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = None
        while n > 0:
            curr = n & 1
            if prev is not None and prev == curr:
                return False
            prev = curr
            n = n >> 1
        return True

    def hasAlternatingBits_1(self, n: int) -> bool:
        return (v := bin(n)[2:]).count('00') == 0 and v.count('11') == 0

    def hasAlternatingBits_2(self, n: int) -> bool:
        return all(p not in bin(n) for p in ('00','11'))

# Main section
for n in [
            5,
            7,
            11,
            1431655765,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.hasAlternatingBits(n)
    r1 = sol.hasAlternatingBits_1(n)
    r2 = sol.hasAlternatingBits_2(n)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print(f'r2 = {r2}')
    assert(r == r1 == r2)
    print('=================================================')
 









