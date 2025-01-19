#
# ===========================================================================================
# Approach 1: Simple brute force since the constraints are small. len(nums1) <= 3000.
#
# Approach 2: Another idea is to store index list for each element and store matches by
# iterating over these index lists. The max of the "matches" list is the answer.
# Eg. index list of element 1 is [1,4] in nums1 and [0,3] in nums2.
# We iterate through all these indexes and store matches in an array. 1->0 = shift of 5,
# 1->3 = shift of 2, 4->0 = shift of 2, 4->3 = shift of 5. So matches=>counts is {5:2, 2:2}.
#
# Approach 3: Simple O(N^2) - iterate over both lists, find sum and max.
# ===========================================================================================
#
from typing import List
from collections import defaultdict

class Solution:
    def maximumMatchingIndices(self, nums1: List[int], nums2: List[int]) -> int:
        def match_count(idx):
            # Given an index "idx", reset nums2 so that it looks like it is
            # shifted "idx" times. Then zip and compare matching elements.
            arr = nums2[idx:] + nums2[:idx]
            return sum([nums1[i] == arr[i] for i in range(N)])
        N = len(nums1)
        res = 0
        for i in range(N):
            res = max(res, match_count(i))
        return res
    def maximumMatchingIndices_1(self, nums1: List[int], nums2: List[int]) -> int:
        indices1 = defaultdict(list)
        for i, v in enumerate(nums1):
            indices1[v] += [i]
        indices2 = defaultdict(list)
        for i, v in enumerate(nums2):
            indices2[v] += [i]
        N = len(nums1)
        # matches[i] is the number of matches after i shifts
        matches = [0 for _ in range(N)]
        for num in indices1:
            for i1 in indices1[num]:
                for i2 in indices2[num]:
                    matches[(i2 - i1) % N] += 1
        return max(matches)
    def maximumMatchingIndices_2(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        res = 0
        for i in range(N):
            cnt = 0
            for j in range(N):
                cnt += nums1[(i + j) % N] == nums2[j]
            res = max(res, cnt)
        return res

# Main section
for nums1, nums2 in [
                       ([3,1,2,3,1,2], [1,2,3,1,2,3]),
                       ([1,4,2,5,3,1], [2,3,1,2,4,6]),
                       ([9,1,2,2,6,7,9,8,5,5,4,7,7,5,8,3,2,10,5,5,3,3,1,2,7,2,3,1,6,9,2,9,6,8,9,10,3,3,9,5,1,7,3,1,4,8,2,6,5,5,7,6,2,4,2,4,7,4,2,9,2,10,10,3,1,10,8,8,5,9,4,8,9,8,4,5,6,5,6,3,8,7,2,5,6,4,9,1,2,4,8,5,2,6,6,6,2,2,2,4], [5,1,10,9,8,9,1,5,5,7,4,7,1,9,6,4,1,3,8,1,6,2,4,2,10,7,10,9,3,2,10,5,8,9,10,9,8,2,1,2,9,9,2,7,2,10,7,6,9,2,3,10,4,6,8,9,10,7,2,3,1,8,7,1,2,8,5,1,2,2,3,5,2,2,1,5,6,3,5,10,8,9,3,5,4,8,8,5,3,6,10,10,6,6,1,10,7,10,1,9]),
                       ([1,2,3,2], [3,2,2,1]),
                    ]:
    print(f'nums1 = {nums1}')
    print(f'nums2 = {nums2}')
    sol = Solution()
    r = sol.maximumMatchingIndices(nums1, nums2)
    print(f'r  = {r}')
    r1 = sol.maximumMatchingIndices_1(nums1, nums2)
    print(f'r1 = {r1}')
    r2 = sol.maximumMatchingIndices_2(nums1, nums2)
    print(f'r2 = {r2}')
    print('=================')


