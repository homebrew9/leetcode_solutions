#
# Concept # 1: x ^ x = 0
# Concept # 2: x ^ 0 = x
# Concept # 3: a ^ b = k
#              => a ^ b ^ b = k ^ b
#              => a ^ (b ^ b) = k ^ b
#              => a ^ 0 = k ^ b        .... by Concept # 1
#              => a = k ^ b            .... by Concept # 2
#              Thus a ^ b = k => a = k ^ b
# Concept # 4: i + (k - i) = k
# Now consider: (x1 ^ x2) + (y1 ^ y2) = k   .... Eqn. 1
# Comparing with Concept # 4, let i = (x1 ^ x2) and (k - i) = y1 ^ y2
# In this case also, Eqn. 1 holds true.
# Now let's find out x2 and y2.
# i = x1 ^ x2       => x2 = i ^ x1
# (k - i) = y1 ^ y2 => y2 = (k - i) ^ y1
# Thus for each (x1, y1), for each i = 0 to k, if we find (x2, y2) in out dictionary,
# then increment the result.
# 
from typing import List
from collections import Counter

class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        #
        # Concept # 1: x ^ x = 0
        # Concept # 2: x ^ 0 = x
        # Concept # 3: a ^ b = k
        #              => a ^ b ^ b = k ^ b
        #              => a ^ (b ^ b) = k ^ b
        #              => a ^ 0 = k ^ b        .... by Concept # 1
        #              => a = k ^ b            .... by Concept # 2
        #              Thus a ^ b = k => a = k ^ b
        # Concept # 4: i + (k - i) = k
        # Now consider: (x1 ^ x2) + (y1 ^ y2) = k   .... Eqn. 1
        # Comparing with Concept # 4, let i = (x1 ^ x2) and (k - i) = y1 ^ y2
        # In this case also, Eqn. 1 holds true.
        # Now let's find out x2 and y2.
        # i = x1 ^ x2       => x2 = i ^ x1
        # (k - i) = y1 ^ y2 => y2 = (k - i) ^ y1
        # Thus for each (x1, y1), for each i = 0 to k, if we find (x2, y2) in out dictionary,
        # then increment the result.
        # 
        ans = 0
        cntr = Counter()
        for x1, y1 in coordinates:
            print(f'\t(x1, y1) = ({x1}, {y1}); ans = {ans}; cntr = {cntr}')
            for i in range(k+1):
                x2 = i ^ x1
                y2 = (k - i) ^ y1
                ans += cntr[(x2, y2)] # Counter value defaults to 0 if (x2,y2) is absent
            cntr[(x1,y1)] += 1
        return ans

# Main section
for coordinates, k in [
                         ([[1,2],[4,2],[1,3],[5,2]], 5),
                         ([[1,3],[1,3],[1,3],[1,3],[1,3]], 0),
                         ([[27,94],[61,68],[47,0],[100,4],[127,89],[61,103],[26,4],[51,54],[91,26],[98,23],[80,74],[19,93]], 95),
                      ]:
    print(f'coordinates, k = {coordinates}, {k}')
    sol = Solution()
    r = sol.countPairs(coordinates, k)
    print(f'r = {r}')
    print('====================')


