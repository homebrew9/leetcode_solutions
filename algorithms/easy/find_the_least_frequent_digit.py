from collections import Counter

class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        cntr = Counter(str(n))
        min_freq = min(cntr.values())
        return min([int(k) for k, v in cntr.items() if v == min_freq])

# Main section
for n in [
            1553322,
            723344511,
            1583230031,
            1307711736,
            378387873,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.getLeastFrequentDigit(n)
    print(f'r = {r}')
    print('==========================')

















