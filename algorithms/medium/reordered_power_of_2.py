import math
from collections import Counter

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        lower = 0
        upper = int(math.log10(10**9)/math.log10(2))
        # Create a hash tables with powers of 2 and their lengths as key-value pairs
        hsh = dict()
        for i in range(upper+1):
            hsh[2**i] = len(str(2**i))
        # Determine all powers of 2 that have the same length as input n and
        # use collections.Counter to determine if the power of 2 and n are anagrams.
        # Since 0 cannot be moved to the beginning while rearranging n, the lengths
        # of all permutations of n will always have the same length as n.
        size = len(str(n))
        for k, v in hsh.items():
            if size == v and Counter(str(n)) == Counter(str(k)):
                return True
        return False

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




