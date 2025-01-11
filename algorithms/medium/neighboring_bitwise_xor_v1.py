# ========================================================================================
# We can try to determine the original list given the derived list.
# Let's say the original list is [a, b, c, d]
# We are given derived list: [a^b, b^c, c^d, d^a]
# Let's assume that origl[0] = 0. Then:
#     drvd[0] = orig[0] ^ orig[1] => orig[1] = drvd[0] ^ orig[0] -> this gives orig[1]
#     drvd[1] = orig[1] ^ orig[2] => orig[2] = drvd[1] ^ orig[1] -> this gives orig[2]
#     drvd[2] = orig[2] ^ orig[3] => orig[3] = drvd[2] ^ orig[2] -> this gives orig[3]
#     drvd[3] = orig[3] ^ orig[0] => orig[0] = drvd[3] ^ orig[3] -> this gives orig[0]
# We then check the value of orig[0] in the last step above with our original assumption
# that orig[0] = 0. If they match, then there is a valid original list, otherwise not.
# 
# But can the original value of orig[0] be 1? Should we test the assumption that orig[0]=1?
# Actually, if there is an original list starting with 0, then there will be an original
# list starting with 1 as well. I don't know the proof of this theorem, but it seems so
# by trial and error. So, we need not test with orig[0] = 1. Just one assumption is enough.
# ========================================================================================
from typing import List

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        def determineOriginal(derived):
            N = len(derived)
            original = [None for _ in range(N)]
            guess = 0
            original[0] = guess
            for i in range(1, N+1):
                pos = i % N
                original[pos] = derived[i-1] ^ original[i-1]
            if original[0] != guess:
                return []
            return original

        orig = determineOriginal(derived)
        return False if len(orig) == 0 else True

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

