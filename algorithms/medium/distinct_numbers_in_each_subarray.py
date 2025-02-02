from typing import List
from collections import defaultdict

class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        # Two-pointer technique that avoids an extra list addition at the end
        N = len(nums)
        hsh = defaultdict(int)
        res = list()
        i, j = 0, 0
        first_k_block = True
        while j < N:
            hsh[nums[j]] += 1
            if j >= k - 1:
                if not first_k_block:
                    hsh[nums[i]] -= 1
                    if hsh[nums[i]] == 0:
                        del hsh[nums[i]]
                    i += 1
                res.append(len(hsh))
                first_k_block = False
            j += 1
        return res

# Main section
for nums, k in [
                  ([1,2,3,2,2,1,3], 3),
                  ([1,1,1,1,2,3,4], 4),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.distinctNumbers(nums, k)
    print(f'r = {r}')
    print('=====================')

