# ===============================================================================
# Let original list be [a, b, c, d, e]
# Then the derived list is [a^b, b^c, c^d, d^e, e^a]
# Hence XOR(derived_list)
#     = (a^b) ^ (b^c) ^ (c^d) ^ (d^e) ^ (e^a)
#     = a ^ (b^b) ^ (c^c) ^ (d^d) ^ (e^e) ^ a
#     = a ^ (0) ^ (0) ^ (0) ^ (0) ^ a
#     = (a ^ 0) ^ (0 ^ 0) ^ (0 ^ a)
#     = (a) ^ (0) ^ (a)
#     = (a ^ 0) ^ a
#     = a ^ a
#     = 0
# So we just find the XOR of the derived list. If that is 0, then it means
# there is a valid original list. Otherwise not.
# ===============================================================================
from typing import List

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        res = 0
        for d in derived:
            res ^= d
        return res == 0
        
# Main section
for derived in [
                  [1,1,0],
                  [1,1],
                  [1,0],
                  [1,0,1,1,1],
                  [0,1,1,1,1],
                  [0,1,1,1,0],
                  [1,1,0,1,1],
               ]:
    print(f'derived = {derived}')
    sol = Solution()
    r = sol.doesValidArrayExist(derived)
    print(f'r = {r}')
    print('======================')


