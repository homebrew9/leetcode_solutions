#
# Notice that if a + b = k, then a%k + b%k = k. Eg. 3 + 7 = multiple of 5.
# So (3%5, 7%5) = (3, 2) which adds up to 5. We simply have to mod all elements.
# Then check that each mod value has its "complement" value. The exception is 0.
# The 0 mod value can correspond to 0, 5, 10, etc. So it must occur even number of times.
#
from typing import List
from collections import defaultdict

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        hsh = defaultdict(int)
        for a in arr:
            i = a % k
            hsh[i] += 1
        for i in range(k):
            if i == 0:
                if hsh[i] % 2 != 0:
                    return False
            else:
                if hsh[i] != hsh[k-i]:
                    return False
        return True

# Main section
for arr, k in [
                 ([1,2,3,4,5,10,6,7,8,9], 5),
                 ([1,2,3,4,5,6], 7),
                 ([1,2,3,4,5,6], 10),
                 ([-7,-7,-6,-6,-3,-1,0,4,8,9], 2),
                 ([-7,-7,-6,-6,-3,-1,0,4,8,22], 2),
              ]:
    print(f'arr, k = {arr}, {k}')
    sol = Solution()
    r = sol.canArrange(arr, k)
    print(f'r = {r}')
    print('===================')


