# ===========================================================================================
# Note that the inner while loop works because each element is greater than 0.
# It will not work if elements can be negative integers. A counterexample is below:
#     nums = [2, -1, 1, 3], target = 4
# In this case, our initial length would be 4 ([2,-1,1,3]) but then when we try to
# minimize the length in the 2nd while loop we will exit at i = 1 because the sum
# is 3 ([-1,1,3]). We exit because the sum (3) has dipped below target (4) and we
# are led to believe that the sum cannot go up from there. However, if we keep going
# then we see that the sum actually goes up; for i = 2 we have [1,3] which is 4 >= 4
# and we find our required answer 2.
#
# The negative value -1 breaks the monotonic sum property that a standard sliding window
# relies on, making a simple variable-length sliding window approach unreliable.
#
# When negative ints are involved, this becomes a Hard problem and can be solved
# with a heap or montonic stack + binary search or deque.
# ===========================================================================================

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        N = len(nums)
        res = float('inf')
        i, j = 0, 0
        curr = 0
        while j < N:
            curr += nums[j]
            while curr >= target:
                res = min(res, j - i + 1)
                curr -= nums[i]
                i += 1
            j += 1
        return 0 if res == float('inf') else res

# Main section
for target, nums in [
                       (7, [2,3,1,2,4,3]),
                       (4, [1,4,4]),
                       (11, [1,1,1,1,1,1,1,1]),
                       (11, [1,2,3,4,5]),
                    ]:
    print(f'target, nums = {target}, {nums}')
    sol = Solution()
    r = sol.minSubArrayLen(target, nums)
    print(f'r = {r}')
    print('=================')


