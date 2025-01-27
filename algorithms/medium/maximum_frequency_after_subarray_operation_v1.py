#
# The idea is similar conceptually to Kadane's algorithm - we test each number, and
# attempt to create a subarray with a maximum "score" by converting each occurrence
# of this number to K. Each time we find the number we're testing, we add 1 point.
# If we find "K", we subtract one point. If this score is negative, there's no point
# in continuing, so we restart at 0 from the next index (Kadane).
#
from typing import List
from collections import Counter

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        N = len(nums)
        cntr = Counter(nums)
        # The default maximum answer is the frequency of k
        ans = cntr[k]
        # Only need 1-50 as per constraints
        for n in range(51):
            # We've already considered n==k in our default answer, and
            # we don't care if n is not in nums
            if n not in cntr or n == k:
                continue
            score, k_count = 0, 0
            for i in range(N):
                if nums[i] == n:
                    score += 1
                elif nums[i] == k:
                    k_count += 1
                # Restart if score is negative
                if k_count > score:
                    score, k_count = 0, 0
                # Subtract number of "k" integers in our subarray from the total number that occur
                ans = max(ans, score + (cntr[k] - k_count))
        return ans

# Main section
for nums, k in [
                  ([1,2,3,4,5,6], 1),
                  ([10,2,3,4,5,5,4,3,2,2], 10),
                  ([10,9,2,4,6,4,2,1,2], 4),
                  ([1,9], 8),
                  ([1,4,9,5,9,1,4,2], 1),
                  ([6,1,6], 1),
                  ([1,16,35,3,32,1,10,34,2,47,2,50,23,23,22,27,18,43,35,30,27,40,17,39,1,34,28,17,43,2,15,31,46,34,35,15,7,33,26,44,45,20,35,40,22,6,41,45,20,25,33,12,15,18,6,48,2,45,26,15,15,37,26,24,32,41,14,35,20,40,5,45,24,10,20,6,18,4,18,7,24,32,27,6,27,5,28,38,38,26,25,35,2,32,31,36,26,19,5,5,18,37,23,47,47,39,49,36,41,43,9,50,3,33,44,43,26,20,21,10,18,11,36,35,3,38,8,4,39,17,15,27,27,8,30,43,18,29,14,29,4,1,1,34,4,33,19,45,18,13,10,48,24,10,26,30,8,12,2,41,43,34,24,25,43,32,31,2,31,29,13,27,24,45,19,41,40,19,39,16,43,39,5,39,42,14,11,39,39,35,14,21,21,15,41,8,3,19,15,21,26,39,33,22,48,12,13,47,29,11,49,25,2,41,37,50,15,4,33,7,9,18,24,29,50,13,40,33,5,50,26,50,37,49,25,49,33,20,50,48,6,13,32,49,46,12,2,22,41,9,26,32,16,8,43,29,36,42,43,23,27,6,24,32,38,25,24,39,28,16,49,39,9,32,20,45,9,19,7,42,22,41,45,14,3,44,25,46,47,19,42,26,6,11,30,26,47,24,19,11,30,24,32,16,14,9,26,9,23,28,12,33,6,42,41,30,15,37,36,43,29,26,37,25,47,8,7,43,45,33,12,43,31,3,40,44,31,7,26,43,6,26,7,50,50,50,22,47,11,31,14,28,41,46,19,45,6,39,3,39,2,36,43,20,41,46,18,38,14,23,15,11,39,20,1,21,47,8,46,25,18,14,41,46,45,41,42,41,41,20,25,43,43,44,48,24,35,35,49,39,35,20,22,13,11,14,43,37,17,26,15,5,22,38,4,22,2,46,48,34,29,37,39,37,6,11,9,9,47,1,14,24,39,34,37,5,11,10,39,49,17,35,15,17,23,3,34,44,10,32,38,22,31,1,42,33,31,28,22,5,16,9,27,3,31,33,3,1,7,8,41,4,34,7,16,43,13,38,26,25,17,2,27,10,19,2,47,19,39,38,27,46,45,9,42,27,43,12,9,48], 19),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.maxFrequency(nums, k)
    print(f'r = {r}')
    print('======================')


