from typing import List

class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        '''
            nums1[i] - nums2[i] > nums2[j] - nums1[j]

                     0   1  2   3               0   1   2  3
            nums1 = [1, 10, 6,  2]   ; nums2 = [1,  4,  1, 5]
                     0   6  5  -3               0  -6  -5  3
                     (0, 1), (0, 2)
                     (1, 2), (1, 3)
                     (2, 3)

           sorted:  [-3, 0, 5,  6]
                    nums1[3] - nums2[3] <=> nums1[1] - nums2[1]  (3, 1)
                    nums1[3] - nums2[3] <=> nums1[2] - nums2[2]  (3, 2)
                    nums1[0] - nums2[0] <=> nums1[2] - nums2[2]  (0, 2)
                    nums1[0] - nums2[0] <=> nums1[1] - nums2[1]  (0, 1)
                    nums1[2] - nums2[2] <=> nums1[1] - nums2[1]  (2, 1)
        '''
        N = len(nums1)
        diff = sorted([nums1[i] - nums2[i] for i in range(N)])
        res = 0
        for i in range(N-1):
            left, right = i + 1, N - 1
            while left <= right:
                mid = (left + right) // 2
                if diff[i] + diff[mid] > 0:
                    right = mid - 1
                else:
                    left = mid + 1
            res += N - left
        return res

# Main section
for nums1, nums2 in [
                       ([2,1,2,1], [1,2,1,2]),
                       ([1,10,6,2], [1,4,1,5]),
                    ]:
    print(f'nums1, nums2 = {nums1}, {nums2}')
    sol = Solution()
    r = sol.countPairs(nums1, nums2)
    print(f'r = {r}')
    print('=================')

