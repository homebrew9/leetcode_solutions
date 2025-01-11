#
# Does not work for last test case.
#
from typing import List

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        N = len(nums1)
        nums1.sort()
        #nums2.sort()
        for i in range(N):
            print(f'\ti, nums1 = {i}, {nums1}')
            left, right = i, i
            while right < N and nums1[right] <= nums2[i]:
                right += 1
            print(f'\tright = {right}')
            #if right >= N:
            #    return nums1
            if right < N:
                nums1[left], nums1[right] = nums1[right], nums1[left]
            print(f'\ti, nums1 = {i}, {nums1}')
            print(f'~~~~')
        return nums1

# Main section
for nums1, nums2 in [
                       #([1,2,3,4], [1,2,3,4]),
                       #([1,9,9,9,1,6,9],[9,4,3,2,1,10,5]),
                       #([31,55,90,71,36,77,41,31,2,14],[82,95,26,79,41,3,85,96,23,91]),
                       ([9,1,2,4,5],[6,2,9,1,4]),
                    ]:
    print(f'nums1, nums2 = {nums1}, {nums2}')
    sol = Solution()
    r = sol.advantageCount(nums1, nums2)
    print(f'r = {r}')
    print('====================')

