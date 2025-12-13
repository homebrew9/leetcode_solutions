from typing import List

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort(reverse=True)
        res = 0
        for a, b in zip(nums1, nums2):
            res += a * b
        return res

# Main section
for nums1, nums2 in [
                       ([5,3,4,2], [4,2,2,5]),
                       ([2,1,4,5,7], [3,2,4,8,6]),
                       ([60,77,43,18,76,38,43,37,97,15,70,89,74,85,33,24,77,75,29,77], [3,95,13,42,43,50,17,25,50,76,26,71,10,42,90,36,37,70,77,2]),
                    ]:
    print(f'nums1, nums2 = {nums1}, {nums2}')
    sol = Solution()
    r = sol.minProductSum(nums1, nums2)
    print(f'r = {r}')
    print('===========================')







































