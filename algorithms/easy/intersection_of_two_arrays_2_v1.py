#
# Ref: https://stackoverflow.com/questions/49775883/common-elements-of-two-lists-including-repetitions
# Pretty straightforward solution. Good to know the capabilities of Counter!
#
from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cntr1 = Counter(nums1)
        cntr2 = Counter(nums2)
        intersect = cntr1 & cntr2
        return list(intersect.elements())

# Main section
sol = Solution()
for nums1, nums2 in [
                       ([1,2,2,1], [2,2]),
                       ([4,9,5], [9,4,9,8,4]),
                       ([4], [9]),
                       ([0], [0]),
                       ([1,2,3,4,5], [1,2,3,4,5]),
                       ([9,9,9,9,9], [9,9,9,9,9]),
                       ([1,2], [1,1]),
                    ]:
    print(f'nums1 = {nums1} ; nums2 = {nums2}')
    r = sol.intersect(nums1, nums2)
    print(f'r = {r}')
    print('======================')


