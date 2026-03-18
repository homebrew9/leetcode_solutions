from typing import List

class Solution:
    def reverseSubarrays(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        span = N // k
        start = 0
        res = list()
        while (end := start + span) < N:
            for i in range(end-1, start-1, -1):
                res.append(nums[i])
            start = end
        for i in range(end-1, start-1, -1):
            res.append(nums[i])
        return res

# Main section
for nums, k in [
                  ([1,2,4,3,5,6], 3),
                  ([5,4,4,2], 1),
               ]:
    print(f'nums = {nums}, k = {k}')
    sol = Solution()
    r = sol.reverseSubarrays(nums, k)
    print(f'r = {r}')
    print('===============================')


