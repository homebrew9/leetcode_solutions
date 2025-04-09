from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums.sort()
        res = 0
        for i in range(N-1, -1, -1):
            if nums[i] < k:
                return -1
            if i < N - 1 and nums[i] != nums[i+1]:
                res += 1
        if nums[0] > k:
            res += 1
        return res

# Main section
for nums, k in [
                  ([5,2,5,4,5], 2),
                  ([2,1,2], 2),
                  ([9,7,5,3], 1),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.minOperations(nums, k)
    print(f'r = {r}')
    print('========================')

