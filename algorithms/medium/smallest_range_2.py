#
# Clear explanation in this article:
# https://jimmy-shen.medium.com/an-interesting-problem-910-smallest-range-ii-302ca119bc8c
#
from typing import List

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        # 1) Sort the vector. Let its length be N.
        # 2) Assume that there is a point at index i. On the left of the point, all elements
        #    add K. On the right of the point, all elements subtract K.
        #    Check each possible point. (a point is between two numbers).
        # 3) Cause there are two segments (A[0]+K, A[1]+K, ..., A[i]+K, A[i+1]-K, ..., A[n]-K).
        #    The first one is on the left of the current point (A[i] + K is the last element of
        #    the first segment). The second one is on the right of the current point
        #    (A[i + 1] - K is the first element of the second segment).
        # 4) For the first segment, the smallest element is "left" (at index 0) and the largest
        #    is A[i] + K. For the second segment, A[i + 1] - K is the smallest element and the
        #    largest is "right" (at index N-1). Thus, for each point, the largest element should
        #    be either A[i] + K or "right". The smallest element should be either "left"
        #    or A[i + 1] - K.
        nums.sort()
        if len(nums) == 1:return 0
        res = nums[-1] - nums[0]
        for i in range(len(nums)-1):
            this_max = max(nums[i]+k, nums[-1]-k)
            this_min = min(nums[0]+k, nums[i+1]-k)
            res = min(res, this_max - this_min)
        return res

# Main section
for nums, k in [
                  ([1], 0),
                  ([0,10], 2),
                  ([1,3,6], 3),
                  ([29,76,75,9,6,84,76,53,87,85,89,59,100,92,83,69,14,71,45,78,2,65,79,49,21,17,37,66,91,46,73,6,93,10,92,25,62,13,69,6,74,57,81,6,35,66,3,11,25,0,85,25,48,53,46,86,94,39,37,37,3,46,40,98,5,15,73,41,70,20,74,14,100,83,56,7,12,44,23,22,0,10,14,69,71,78,72,61,90,76,34,27,1,19,38,79,15,79,2,25,79,65,50,90,95,81,48,91,65,22,85,4,77,89,69,26,51,3,16,26,75,62,67,74,97,61,42,80,5,59,74,84,23,97,78,24,65,87,52,72,18,0,35,93,68,35,57,76,20,34,76,91,53,50,55,21,48,94,18,38,99,17,15,76,46,64,0,49,85,12,89,54,20,70,28,51,21,3,86,79,44,69,95,14,47,72,35,33,6,61,75,99,87,32,49,69,11,9,68,85,86,12,42,90,76,41,78,51,38,69,83,80,12,60,28,24,53,35,19,57,67,5,48,5,55,92,71,93,64,44,51,87,61,20,64,99,19,33,60,59,11,66,37,34,46,53,21,66,43,18,23,17,36,66,74,95,30,23,23,77,74,4,64,100,16,45,61,5,60,45,60,67,68,14,88,49,31,36,65,63,15,77,89,8,56,12,53,71,28,1,65,81,86,21,64,42,34,36,8,0], 3),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.smallestRangeII(nums, k)
    print(f'r = {r}')
    print('=================')

