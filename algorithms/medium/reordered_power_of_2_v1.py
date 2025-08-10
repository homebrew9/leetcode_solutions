from collections import Counter

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        seen = set()
        p = 1
        while p <= 10**9:
            seen.add(tuple(sorted(Counter(str(p)).elements())))
            p *= 2
        return tuple(sorted(Counter(str(n)).elements())) in seen

# Main section
sol = Solution()
for n in [
            1,
            10,
            9064,
            1250279,
            1250278,
            16777216,
            67121767,
            536870912,
            123506789,
            124506789,
            123506799,
         ]:
    print(f'n = {n}')
    r = sol.reorderedPowerOf2(n)
    print(f'r = {r}')
    print('======================')


























