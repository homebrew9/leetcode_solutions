from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # We simply apply the "merge" function of the MergeSort algorithm!
        res = list()
        N, M = len(nums1), len(nums2)
        i, j = 0, 0
        while i < N and j < M:
            a, b = nums1[i]
            c, d = nums2[j]
            if a == c:
                res.append([a, b + d])
                i += 1
                j += 1
            elif a < c:
                res.append([a, b])
                i += 1
            elif a > c:
                res.append([c, d])
                j += 1
        while i < N:
            res.append(nums1[i])
            i += 1
        while j < M:
            res.append(nums2[j])
            j += 1
        return res

# Main section
for nums1, nums2 in [
                       ([[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]]),
                       ([[2,4],[3,6],[5,5]], [[1,3],[4,3]]),
                    ]:
    print(f'nums1 = {nums1}')
    print(f'nums2 = {nums2}')
    sol = Solution()
    r = sol.mergeArrays(nums1, nums2)
    print(f'r     = {r}')
    print('================================')

