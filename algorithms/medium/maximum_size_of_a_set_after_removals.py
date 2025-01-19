from typing import List

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        We only need to work with sets. Let nums1 = [2,2,2,3], nums2 = [1,2,2,2]
        Venn diagram of their intersection: [3][2][1]
        Max elements we can keep from nums1: v1 = min(len(nums1_set)-len_both, N/2) = 1
        Max elements we can keep from nums2: v2 = min(len(nums2_set)-len_both, N/2) = 1
        So final result = min(v1 + v2 + len_both, N) i.e. min of universal set and array length
        '''
        N = len(nums1)
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        len_both = len(nums1_set & nums2_set)

        print(nums1_set, nums2_set, len_both)
        
        v1 = min(len(nums1_set) - len_both, N//2)
        v2 = min(len(nums2_set) - len_both, N//2)
        
        print(v1, v2, N)

        return min(v1 + v2 + len_both, N)

# Main section
for nums1, nums2 in [
                       ([1,2,1,2], [1,1,1,1]),
                       ([1,2,3,4,5,6], [2,3,2,3,2,3]),
                       ([1,1,2,2,3,3], [4,4,5,5,6,6]),
                       ([2,2,2,3], [1,2,2,2]),
                       ([1,2,3,4,5,6,7,8,9,10], [2,2,3,3,7,7,8,9,1,10]),
                    ]:
    print(f'nums1 = {nums1} ; nums2 = {nums2}')
    sol = Solution()
    r = sol.maximumSetSize(nums1, nums2)
    print(f'r = {r}')
    print('======================')


