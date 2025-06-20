from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums.sort()
        res = 1
        i, j = 0, 0
        while j < N:
            if nums[j] - nums[i] > k:
                i = j
                res += 1
            j += 1
        return res

# Main section
for nums, k in [
                  ([3,6,1,2,5], 2),
                  ([1,2,3], 1),
                  ([2,2,4,5], 0),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.partitionArray(nums, k)
    print(f'r = {r}')
    print('===========================')


