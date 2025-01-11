from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))

# Main section
sol = Solution()
for nums1, nums2 in [
                       [ [1,2,2,1], [2,2] ],
                       [ [4,9,5], [9,4,9,8,4] ],
                       [ [3], [1,2,3] ],
                       [ [1,2,3], [4,5,6] ],
                       [ [1], [9] ],
                    ]:
    print(f'nums1 = {nums1} ; nums2 = {nums2}')
    r = sol.intersection(nums1, nums2)
    print(f'r = {r}')
    print('======================')

