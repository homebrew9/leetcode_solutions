from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        N1, N2 = len(nums1), len(nums2)
        i, j = 0, 0
        while i < N1 and j < N2:
            if nums1[i] == nums2[j]:
                return nums1[i]
            if nums1[i] < nums2[j]:
                i += 1
            elif nums2[j] < nums1[i]:
                j += 1
        return -1

# Main section
for nums1, nums2 in [
                       ([1,2,3], [2,4]),
                       ([1,2,3,6], [2,3,4,5]),
                    ]:
    print(f'nums1, nums2 = {nums1}, {nums2}')
    sol = Solution()
    r = sol.getCommon(nums1, nums2)
    print(f'r = {r}')
    print('==========================')


