#
# Doesn't work for the last test case.
# Correct answer is 7, this algorithm returns 11.
#
from typing import List

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        prev = nums[-1]
        for i in range(N-2, -1, -1):
            curr = nums[i]
            while curr > prev:
                # Split curr into two parts: low and high
                # low should be as large as possible, but not more than prev
                # Keep splitting at the current index until we are done.
                if curr%2 == 1:
                    low, high = curr//2, curr//2+1
                else:
                    low, high = curr//2, curr//2
                if low > prev:
                    diff = low - prev
                    low -= diff
                    high += diff
                    curr, prev = high, low
                else:
                    curr, prev = low, high
                res += 1
            prev = curr
        return res

# Main section
for nums in [
               [2,7,9,5,8,8],
               [1,2,3,7,9,5,6],
               [3,9,3],
               [1,2,3,4,5],
               [82,62,38,8,65,83,68,68,91,58],
               [82,62,38],
               [3,29,28],
               [3,60,28],
               [100,82,100,49],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.minimumReplacement(nums)
    print(f'r = {r}')
    print('======================')

