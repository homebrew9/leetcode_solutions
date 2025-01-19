# ===========================================================================================
# Note that if all elements are > 0 then the solution can be derived using a Sliding Window
# approach. That is a medium problem. It is trickier when negative ints are introduced. Eg.
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
import heapq

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        h = list()
        heapq.heapify(h)
        res = float('inf')
        curr = 0
        for i, v in enumerate(nums):
            curr += v
            if curr >= k:
                res = min(res, i + 1)
            while h and curr - h[0][0] >= k:
                cs, ind = heapq.heappop(h)
                res = min(res, i - ind)
            heapq.heappush(h, (curr, i))
        return -1 if res == float('inf') else res

# Main section
for nums, k in [
                  ([1], 1),
                  ([1,2], 4),
                  ([2,-1,2], 3),
                  ([2,-1,2,1], 3),
                  ([2,-1,1,3], 4),
                  ([-1,-2,4,8,4,-4,10,-2,-3,9,2,-4,-3,-1,-9,-3,-5,4,-8,-6], 11),
                  ([5,5,0,-2,-1,-2,1,3,1,-5,3,-10,-10,-4,-6,4,5,2,-10,-6], 7),
                  ([-9,-2,8,0,-9,-5,10,4,-4,4,-1,5,-1,-10,-9,4,-4,-5,9,5,7,6,-4,-9,6,10,4,-5,8,-5,-2,3,-7,3,0,8,-10,0,-10,5,-9,-7,-4,10,4,5,4,3,3,8,-8,-7,-4,10,-1,6,3,-9,-3,-6,-2,3,4,7,-9,4,1,3,1,10,-8,-6,-7,5,4], 13),
                  ([9,2,8,0,9,5,10,4,4,4,1,5,1,10,9,4,4,5,9,5,7,6,4,9,6,10,4,5,8,5,2,3,7,3,0,8,10,0,10,5,9,7,4,10,4,5,4,3,3,8,8,7,4,10,1,6,3,9,3,6,2,3,4,7,9,4,1,3,1,10,8,6,7,5,4], 13),
                  ([8,3,9,1,2,4,6,1,1,6,1,8,6,9,4,9,6,3,8,8,4,4,10,7,2,7,5,5,10,1,2,6,3,6,3,2,1,1,1,8,6,6,10,2,1,2,5,3,7,5,5,9,1,5,5,9,9,2,2,4,2,9,9,5,10,0,10,9,3,9,9,6,4,1,9,8,5,6,7,5,9,6,5,6,3,6,5,8,5,5,0,3,7,4,6,10,6,9,4,7], 17),
                  ([1,1,6,1,8,6,9,4,9,6,3,8,8,4,4,10,7,2,7,5,5,10], 17),
                  ([-9,4,-4,-5,9,5,7,6,-4,-9,6,10], 13),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.shortestSubarray(nums, k)
    print(f'r = {r}')
    print('===================')


