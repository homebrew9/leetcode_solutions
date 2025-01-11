from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time complexity is O(nlog(n)). But it should be less than that.
        cntr = Counter(nums)
        arr = sorted(cntr.items(), key=lambda x: x[1], reverse=True)
        return [x for x, y in arr[:k]]

# Main section
for nums, k in [
                  ([1,1,1,2,2,3], 2),
                  ([1], 1),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.topKFrequent(nums, k)
    print(f'r = {r}')
    print('==============')

