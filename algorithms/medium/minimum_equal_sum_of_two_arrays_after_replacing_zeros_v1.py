from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, zeros1 = 0, 0
        sum2, zeros2 = 0, 0
        for n in nums1:
            sum1 += n
            if n == 0:
                sum1 += 1
                zeros1 += 1
        for n in nums2:
            sum2 += n
            if n == 0:
                sum2 += 1
                zeros2 += 1
        if (zeros1 == 0 and sum2 > sum1) or (zeros2 == 0 and sum1 > sum2):
            return -1
        return max(sum1, sum2)


# Main section
for nums1, nums2 in [
                       ([3,2,0,1,0], [6,5,0]),
                       ([2,0,2,0], [1,4]),
                       ([20,0,18,11,0,0,0,0,0,0,17,28,0,11,10,0,0,15,29], [16,9,25,16,1,9,20,28,8,0,1,0,1,27]),
                       ([8,13,15,18,0,18,0,0,5,20,12,27,3,14,22,0], [29,1,6,0,10,24,27,17,14,13,2,19,2,11]),
                       ([0,17,20,17,5,0,14,19,7,8,16,18,6], [21,1,27,19,2,2,24,21,16,1,13,27,8,5,3,11,13,7,29,7]),
                    ]:
    print(f'nums1, nums2 = {nums1}, {nums2}')
    sol = Solution()
    r = sol.minSum(nums1, nums2)
    print(f'r = {r}')
    print('============================')

