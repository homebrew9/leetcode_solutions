from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        N = len(nums)
        inds = [i for i, v in enumerate(nums) if v == key]
        seen = set()
        for ind in inds:
            seen.update([i for i in range(ind - k, ind + k + 1) if 0 <= i < N])
        return sorted(seen)

# Main section
for nums, key, k in [
                       ([3,4,9,1,3,9,5], 9, 1),
                       ([2,2,2,2,2], 2, 2),
                    ]:
    print(f'nums, key, k = {nums}, {key}, {k}')
    sol = Solution()
    r = sol.findKDistantIndices(nums, key, k)
    print(f'r = {r}')
    print('=======================')







