from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def check_for_median(nums):
            if len(nums) == mid_point + 1:
                if is_odd:
                    return (True, nums[-1])
                else:
                    return (True, (nums[-1] + nums[-2]) / 2)
            return (False, None)

        def return_median(nums1, nums2):
            nums = list()
            N, M = len(nums1), len(nums2)
            i, j = 0, 0
            while i < N or j < M:
                if i < N and j < M:
                    if nums1[i] <= nums2[j]:
                        nums.append(nums1[i])
                        i += 1
                    elif nums2[j] < nums1[i]:
                        nums.append(nums2[j])
                        j += 1
                elif i < N:
                    nums.append(nums1[i])
                    i += 1
                elif j < M:
                    nums.append(nums2[j])
                    j += 1
                is_valid, median = check_for_median(nums)
                if is_valid:
                    return median

        size = len(nums1) + len(nums2)
        is_odd = (size % 2 == 1)
        mid_point = size // 2
        res = return_median(nums1, nums2)
        return res

# Main section
for nums1, nums2 in [
                       ([1,3], [2]),
                       ([1,2], [3,4]),
                       ([], [1]),
                       ([9], []),
                       ([-7,-6,-5,-4,-3], [11,18,53,90,103]),
                    ]:
    print(f'nums1, nums2 = {nums1}, {nums2}')
    sol = Solution()
    r = sol.findMedianSortedArrays(nums1, nums2)
    print(f'r = {r}')
    print('====================')


