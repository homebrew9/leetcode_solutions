#
# Review of the basic properties of XOR operator helps us here.
# XOR is both commutative and distributive, i.e. a^b = b^a and (a^b)^c = a^(b^c)
# Also a^a = 0. So if exactly one array has even length then the elements of
# the other array will get canceled out due to the XOR. If both arrays are of odd
# length then we will have one copy of each array that we have to XOR finally.
#
from typing import List
from functools import reduce

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        def xor_list(arr):
            ans = 0
            for n in arr:
                ans ^= n
            return ans
        N, M = len(nums1), len(nums2)
        if N % 2 == 0 and M % 2 == 0:
            return 0
        if N % 2 == 0:
            return xor_list(nums1)
        if M % 2 == 0:
            return xor_list(nums2)
        return xor_list(nums1 + nums2)
    def xorAllNums_1(self, nums1: List[int], nums2: List[int]) -> int:
        def xor_list(arr):
            # A functional approach to determining XOR of an array
            return reduce(lambda x,y: x^y, arr)
        N, M = len(nums1), len(nums2)
        if N % 2 == 0 and M % 2 == 0:
            return 0
        if N % 2 == 0:
            return xor_list(nums1)
        if M % 2 == 0:
            return xor_list(nums2)
        return xor_list(nums1 + nums2)

# Main section
for nums1, nums2 in [
                       ([2,1,3], [10,2,5,0]),
                       ([1,2], [3,4]),
                       ([13,19,21], [56,90,101,103,146]),
                    ]:
    print(f'nums1, nums2 = {nums1}, {nums2}')
    sol = Solution()
    r = sol.xorAllNums(nums1, nums2)
    print(f'r  = {r}')
    r1 = sol.xorAllNums_1(nums1, nums2)
    print(f'r1 = {r1}')
    assert(r == r1)
    print('==================')


