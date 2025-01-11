from typing import List
from sortedcontainers import SortedList

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        sl = SortedList()
        res = 0
        left = 0
        for right in range(N):
            sl.add(nums[right])
            # Important - as long as the end values of the SortedList differ
            # by more than 2, keep removing elements from nums from the left!!
            while left <= right and sl[-1] - sl[0] > 2:
                sl.remove(nums[left])
                left += 1
            res += right - left + 1
        return res

# Main section
for nums in [
               [5,4,2,4],
               [1,2,3],
               [2,3,4,3,3,2],
               [2,3,4,3,3,2,1],
               [5,4,4,4,4,2,4],
               [10,9,8,1,1],
               [1,1,1,1,1],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.continuousSubarrays(nums)
    print(f'r = {r}')
    print('===================')

