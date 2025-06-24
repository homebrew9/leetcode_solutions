from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    # Binary search + Binary Search
    # TC = O(n1 * log(n2) * log(C)), where C = 2*10**10 + 1 is the size of the range of product of the two array elements
    # SC = O(1)
    def f(self, nums2: List[int], x1: int, v: int) -> int:
        if x1 > 0:
            return bisect_right(nums2, v // x1)
        elif x1 < 0:
            return len(nums2) - bisect_left(nums2, -(-v // x1))
        else:
            return len(nums2) if v >= 0 else 0

    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n1 = len(nums1)
        left, right = -(10**10), 10**10
        while left <= right:
            mid = (left + right) // 2
            count = 0
            for i in range(n1):
                count += self.f(nums2, nums1[i], mid)
            if count < k:
                left = mid + 1
            else:
                right = mid - 1
        return left

# Main section
for nums1, nums2, k in [
                          ([2,5], [3,4], 2),
                          ([-4,-2,0,3], [2,4], 6),
                          ([-2,-1,0,1,2], [-3,-1,2,4,5], 3),
                       ]:
    print(f'nums1, nums2, k = {nums1}, {nums2}, {k}')
    sol = Solution()
    r = sol.kthSmallestProduct(nums1, nums2, k)
    print(f'r = {r}')
    print('=======================')

