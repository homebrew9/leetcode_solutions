from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # This is Binary Search problem!
        def is_valid(capability):
            i = 0
            count = 0
            while i < len(nums):
                if nums[i] <= capability:
                    i += 2
                    count += 1
                else:
                    i += 1
                if count == k:
                    break
            return count == k
        l, r = min(nums), max(nums)
        res = 0
        while l <= r:
            m = (l + r) // 2
            if is_valid(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res

# Main section
for nums, k in [
                  ([2,3,5,9], 2),
                  ([2,7,9,3,1], 2),
                  ([35,82,85,60,48,21,59,81,2,12,42,33,6,57,34,25,86,36,70,11,11,8,94,85,22,76,19,50,85,79], 13),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.minCapability(nums, k)
    print(f'r = {r}')
    print('======================')

