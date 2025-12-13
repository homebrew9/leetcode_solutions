from itertools import combinations

class Solution:
    def countTriples(self, n: int) -> int:
        return 2 * sum([a*a + b*b - c*c == 0 for a, b, c in combinations(range(1, n + 1), 3)])

    def countTriples_1(self, n: int) -> int:
        res = 0
        for a in range(1, n - 1):
            for b in range(a + 1, n):
                for c in range(b + 1, n + 1):
                    if a * a + b * b - c * c == 0:
                        res += 2
        return res

# Main section
for n in [
            5,
            10,
            50,
            200,
            250,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.countTriples(n)
    r1 = sol.countTriples_1(n)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    assert(r == r1)
    print('===========================')

















