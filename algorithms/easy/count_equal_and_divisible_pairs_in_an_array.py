from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        N = len(nums)
        res = 0
        for i in range(N):
            for j in range(i+1, N):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    res += 1
        return res

# Main section
for nums, k in [
                  ([3,1,2,2,2,1,3], 2),
                  ([1,2,3,4], 1),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.countPairs(nums, k)
    print(f'r = {r}')
    print('=============')

