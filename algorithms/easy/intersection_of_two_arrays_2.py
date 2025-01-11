from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = list()
        nums1.sort()
        nums2.sort()
        while nums1 and nums2:
            if nums1[-1] > nums2[-1]:
                nums1.pop()
            elif nums2[-1] > nums1[-1]:
                nums2.pop()
            else:
                result.append(nums1[-1])
                nums1.pop()
                nums2.pop()
        return result

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

