#
# Algorithm does not work!
#
from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        cnt = 0
        prd = 1
        left = 0
        if nums[0] < k:
            cnt += 1
            prd = nums[0]
        print(f'\tcnt, prd, left = {cnt}, {prd}, {left}')
        for i in range(1, len(nums)):
            print(f'\t\ti, nums[i] = {i}, {nums[i]}')
            if nums[i] < k:
                cnt += 1
            prd *= nums[i]
            if prd < k:
                cnt += 1
            else:
                while left < i and prd >= k:
                    prd //= nums[left]
                    left += 1
                if prd < k:
                    cnt += 1
            print(f'\t\tprd, cnt = {prd}, {cnt}')
            print(f'\t\tleft = {left}')
            print(f'\t=====')
        while left < i-1:
            prd //= nums[left]
            left += 1
            if prd < k:
                cnt += 1
        return cnt

# Main section
for nums, k in [
                  #([10,5,2,6], 100),
                  #([1,2,3], 0),
                  #([2,3,4], 24),
                  ([2,2,2,2], 24),
                  ([2,2,2,31,2,3], 24),
                  ([2,3,4,31,2,3], 24),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.numSubarrayProductLessThanK(nums, k)
    print(f'r = {r}')
    print('=================')

