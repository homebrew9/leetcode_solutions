from typing import List
import bisect

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        N = len(nums)
        nums.sort()
        res = 0
        for i in range(N):
            left, right = i, N - 1
            while left <= right:
                mid = (left + right) // 2
                val = nums[i] + nums[mid]
                if val <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            #print(f'\ti, right = {i}, {right}')
            #print(bisect.bisect_right(nums, target - nums[i]) - 1)
            if right >= i:
                res += 2**(right - i)
        return res % MOD

# Main section
for nums, target in [
                       ([3,5,6,7], 9),
                       ([3,3,6,8], 10),
                       ([2,3,3,4,6,7], 12),
                       ([1,2,3,4,5,6], 6),
                       ([1,2,3,4,5,6,7,8,9], 7),
                       ([5,2,4,1,7,6,8], 16),
                    ]:
    print(f'nums, target = {nums}, {target}')
    sol = Solution()
    r = sol.numSubseq(nums, target)
    print(f'r = {r}')
    print('=====================')

