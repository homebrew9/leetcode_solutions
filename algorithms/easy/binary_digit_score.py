class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        def set_bit_count(n):
            res = 0
            while n > 0:
                q, r = divmod(n, 2)
                res += r
                n = q
            return res
        s1 = set_bit_count(a)
        s2 = set_bit_count(b)
        return s1 * s2 if s1 >= s2 else s2 // s1

    def calculateScore_1(self, a: int, b: int) -> int:
        def count_set_bits(n):
            res = 0
            while n > 0:
                n &= n - 1 # Clear the lowest set bit
                res += 1
            return res
        s1 = count_set_bits(a)
        s2 = count_set_bits(b)
        return s1 * s2 if s1 >= s2 else s2 // s1

    def calculateScore_2(self, a: int, b: int) -> int:
        # Python 3.10+
        s1 = a.bit_count()
        s2 = b.bit_count()
        return s1 * s2 if s1 >= s2 else s2 // s1

# Main section
for a, b in [
               (14, 6),
               (5, 15),
               (10, 12),
               (93, 71),
            ]:
    print(f'a, b = {a}, {b}')
    sol = Solution()
    r = sol.calculateScore(a, b)
    r1 = sol.calculateScore_1(a, b)
    r2 = sol.calculateScore_2(a, b)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print(f'r2 = {r2}')
    print('===================================')





















