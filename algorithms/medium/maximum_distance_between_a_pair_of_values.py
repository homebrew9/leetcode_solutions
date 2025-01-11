from typing import List

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        max_dist = float('-inf')
        for i in range(len(nums1)):
            n = nums1[i]
            print(f'\ti, n = {i}, {nums1[i]}')
            if i >= len(nums2):
                break
            if nums2[i] < n:
                continue
            low, high = i, len(nums2) - 1
            print(f'\tlow, high = {low}, {high}')
            while low <= high:
                mid = (low + high) // 2
                if nums2[mid] < n:
                    high = mid - 1
                else:
                    low = mid + 1
                print(f'\t\tlow, mid, high = {low}, {mid}, {high}')
            print(f'\tlow, high, mid, nums2[mid] = {low}, {high}, {mid}, {nums2[mid]}')
            curr_dist = high - i
            if curr_dist > max_dist:
                max_dist = curr_dist
            print(f'\tmax_dist = {max_dist}')
            print(f'\t================')
        if max_dist == float('-inf'):
            return 0
        return max_dist

# Main section
for nums1, nums2 in [
                       #([55,30,5,4,2], [100,20,10,10,5]),
                       #([2,2,2], [10,10,1]),
                       #([30,29,19,5], [25,25,25,25,25]),
                       #([8,7,6,5,4,3,2,1], [8,8,8,7,7,7,7,6]),
                       #([5,4], [3,2]),
                       ([9819,9508,7398,7347,6337,5756,5493,5446,5123,3215,1597,774,368,313], [9933,9813,9770,9697,9514,9490,9441,9439,8939,8754,8665,8560]),
                    ]:
    print(f'nums1, nums2 = {nums1}, {nums2}')
    sol = Solution()
    r = sol.maxDistance(nums1, nums2)
    print(f'r = {r}')
    print('==============')

